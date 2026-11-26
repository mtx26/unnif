from scipy.optimize import linprog
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.io import loadmat
from pathlib import Path

fichier = Path(__file__).parent / "data_small_roads (1).mat"
donnees = loadmat(fichier)

G = donnees["G"].toarray()
mu = donnees["mu"].ravel()

epsilon = 0.1



n = G.shape[0]  # Nombre de lignes
mu_cible = (1 - epsilon) * mu + epsilon * np.ones(n) / n

omega = []  # Au départ, aucune position enregistrée
# [(i, j) pour tous les i et j tels que G[i, j] > 0 ou i == j]
for i in range(n):
    for j in range(n):
        if G[i, j] > 0 or i == j:
            omega.append((i, j))
# Définir les coefficients de la fonction objectif
# T, delta +, delta -, A, B, C
m = len(omega)


c = [1] * m + [0] * (5 * m)
# [1, 1, 1,    0, 0, 0,    0, 0, 0,    0, 0, 0,    0, 0, 0]  (exemple pour m=3 et n=3)

A_eq = []
b_eq = []


# G[i, j] + delta_plus[i, j] - delta_moins[i, j] - A[i, j] = 0, pour (i, j) dans omega
for k in range(m):
    i, j = omega[k]

    ligne = [0] * (6 * m)

    ligne[m + k] = 1 # delta +
    ligne[2 * m + k] = -1 # delta -
    ligne[3 * m + k] = -1 # A

    A_eq.append(ligne)
    b_eq.append(-G[i, j])


# Pour chaque ligne i : somme_j(delta_plus[i, j] - delta_moins[i, j]) = 0
# Forme matricielle : (delta_plus - delta_moins) @ 1 = 0
for i in range(n):
    ligne = [0] * (6 * m)

    for k in range(m):
        ligne_i, colonne_j = omega[k]

        if ligne_i == i:
            ligne[m + k] = 1 # delta +
            ligne[2 * m + k] = -1 # delta -

    A_eq.append(ligne)
    b_eq.append(0)


# mu_cible.T @ (G + delta_plus - delta_moins) = mu_cible.T
# Pour chaque colonne j : somme_i(mu_cible[i] * (delta_plus[i, j] - delta_moins[i, j]))
#     = mu_cible[j] - somme_i(mu_cible[i] * G[i, j])
for j in range(n):
    ligne = [0] * (6 * m)

    for k in range(m):
        ligne_i, colonne_j = omega[k]

        if colonne_j == j:
            ligne[m + k] = mu_cible[ligne_i] # delta + pondéré par mu_cible[ligne_i]
            ligne[2 * m + k] = -mu_cible[ligne_i] # delta - pondéré par mu_cible[ligne_i]

    membre_droit = mu_cible[j] - mu_cible @ G[:, j]

    A_eq.append(ligne)
    b_eq.append(membre_droit)

# T[i, j] - delta_plus[i, j] + delta_moins[i, j] - B[i, j] = 0, pour (i, j) dans omega
for k in range(m):
    ligne = [0] * (6 * m)

    ligne[k] = 1
    ligne[m + k] = -1
    ligne[2 * m + k] = 1
    ligne[4 * m + k] = -1

    A_eq.append(ligne)
    b_eq.append(0)

# T[i, j] + delta_plus[i, j] - delta_moins[i, j] - C[i, j] = 0, pour (i, j) dans omega
for k in range(m):
    ligne = [0] * (6 * m)

    ligne[k] = 1
    ligne[m + k] = 1
    ligne[2 * m + k] = -1
    ligne[5 * m + k] = -1

    A_eq.append(ligne)
    b_eq.append(0)


# Contrainte : delta_plus[i, j] = delta_moins[i, j] = 0 hors de omega.
# Imposee par construction : seules les positions dans omega ont des inconnues.

delta = np.zeros((n, n))
# [[0,0, 0],
#  [0,0, 0],
#  [0,0, 0]]


# T, delta_plus, delta_moins, A, B, C >= 0
resultat = linprog(
    c,
    A_eq=A_eq,
    b_eq=b_eq,
    bounds=(0, None),
    method="highs"
)

if not resultat.success:
    raise RuntimeError(resultat.message)

for k, (i, j) in enumerate(omega):
    delta[i, j] = resultat.x[m + k] - resultat.x[2 * m + k]


g_v = G + delta
tolerance = 1e-9

# 1. Les probabilites doivent etre positives ou nulles.
minimum = g_v.min()
if minimum < -tolerance:
    raise ValueError("La matrice de transition modifiée contient des éléments négatifs.")

# 2. La somme de chaque ligne doit etre egale a 1.
for i in range(n):
    somme = g_v[i, :].sum()
    if not math.isclose(somme, 1, abs_tol=tolerance, rel_tol=0):
        raise ValueError(f"La ligne {i} de la matrice de transition modifiée ne somme pas à 1.")

# 3. La distribution cible doit etre stationnaire pour G + delta.
mu_cible_T = mu_cible.reshape(1, n)  # mu_cible transposée sous forme de matrice 1 x n
mu_cible_T_G = mu_cible_T @ g_v
erreur_stationnarite = np.max(np.abs(mu_cible_T_G - mu_cible_T))
if not np.allclose(mu_cible_T_G, mu_cible_T, atol=tolerance, rtol=0):
    raise ValueError("La distribution cible n'est pas stationnaire.")

print("Valeur optimale :", resultat.fun)
print("G :")
print(G)
print("Delta :")
print(delta)
print("Matrice de transition modifiee G + Delta :")
print(g_v)
print("Distribution initiale :", mu)
print("Distribution cible :", mu_cible)

transitions_modifiees = [
    (i, j) for i, j in omega if abs(delta[i, j]) > tolerance
]
transitions_modifiees.sort(key=lambda position: abs(delta[position]), reverse=True)


nombre_modifiees = len(transitions_modifiees)
print(f"Nombre de transitions modifiees : {nombre_modifiees}")
print(f"Pourcentage : {100 * nombre_modifiees / len(omega)}%")

etats = np.arange(1, n + 1)
plt.plot(etats, mu, label="Distribution initiale")
plt.plot(etats, mu_cible, label="Distribution cible")
plt.xlabel("Etat")
plt.ylabel("Proportion stationnaire")
plt.title("Comparaison des distributions")
plt.legend()
plt.tight_layout()
plt.savefig("bac_2/OL/projet/comparaison_distributions.png")
plt.show()
