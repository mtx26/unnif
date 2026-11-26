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

def resoudre(epsilon):
    n = G.shape[0]
    mu_cible = (1 - epsilon) * mu + epsilon * np.ones(n) / n

    omega = []
    for i in range(n):
        for j in range(n):
            if G[i, j] > 0 or i == j:
                omega.append((i, j))

    m = len(omega)
    # Variables : T, delta_plus, delta_moins, A, B, C.
    c = [1] * m + [0] * (5 * m)
    A_eq = []
    b_eq = []

    # G[i, j] + delta_plus[i, j] - delta_moins[i, j] - A[i, j] = 0
    for k in range(m):
        i, j = omega[k]
        ligne = [0] * (6 * m)
        ligne[m + k] = 1
        ligne[2 * m + k] = -1
        ligne[3 * m + k] = -1
        A_eq.append(ligne)
        b_eq.append(-G[i, j])

    # Pour chaque ligne i : somme_j(delta_plus[i, j] - delta_moins[i, j]) = 0
    for i in range(n):
        ligne = [0] * (6 * m)
        for k in range(m):
            ligne_i, colonne_j = omega[k]
            if ligne_i == i:
                ligne[m + k] = 1
                ligne[2 * m + k] = -1
        A_eq.append(ligne)
        b_eq.append(0)

    # mu_cible.T @ (G + delta_plus - delta_moins) = mu_cible.T
    for j in range(n):
        ligne = [0] * (6 * m)
        for k in range(m):
            ligne_i, colonne_j = omega[k]
            if colonne_j == j:
                ligne[m + k] = mu_cible[ligne_i]
                ligne[2 * m + k] = -mu_cible[ligne_i]
        A_eq.append(ligne)
        b_eq.append(mu_cible[j] - mu_cible @ G[:, j])

    # T[i, j] - delta_plus[i, j] + delta_moins[i, j] - B[i, j] = 0
    for k in range(m):
        ligne = [0] * (6 * m)
        ligne[k] = 1
        ligne[m + k] = -1
        ligne[2 * m + k] = 1
        ligne[4 * m + k] = -1
        A_eq.append(ligne)
        b_eq.append(0)

    # T[i, j] + delta_plus[i, j] - delta_moins[i, j] - C[i, j] = 0
    for k in range(m):
        ligne = [0] * (6 * m)
        ligne[k] = 1
        ligne[m + k] = 1
        ligne[2 * m + k] = -1
        ligne[5 * m + k] = -1
        A_eq.append(ligne)
        b_eq.append(0)

    # Hors de omega, delta_plus et delta_moins sont nuls par construction.
    matrice_contraintes = np.asarray(A_eq, dtype=float)

    resultat = linprog(
        c, A_eq=matrice_contraintes, b_eq=b_eq,
        bounds=(0, None), method="highs"
    )
    if not resultat.success:
        raise RuntimeError(f"Echec pour epsilon = {epsilon} : {resultat.message}")
    return resultat, omega, mu_cible, matrice_contraintes


epsilon = 0.1
resultat, omega, mu_cible, matrice_contraintes = resoudre(epsilon)
n = G.shape[0]
m = len(omega)


#calcul de delta à partir de la solution optimale avec la methode linprog
delta = np.zeros((n, n))
for k in range(m):
    i, j = omega[k]
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

# Verification du sommet pour la solution de la forme standard.
solution = resultat.x

# On garde les colonnes correspondant aux variables positives.
indices_positifs = np.flatnonzero(solution > tolerance)
nombre_positives = len(indices_positifs)
colonnes_positives = matrice_contraintes[:, indices_positifs]

if nombre_positives == 0:
    rang = 0
else:
    rang = np.linalg.matrix_rank(colonnes_positives)

print(f"Variables positives : {nombre_positives}")
print(f"Rang des colonnes correspondantes : {rang}")
if rang == nombre_positives:
    print("La solution est un sommet, a la precision numerique pres.")
else:
    print("Le critere numerique de sommet n'est pas verifie.")

etats = np.arange(1, n + 1)
plt.plot(etats, mu, label="Distribution initiale")
plt.plot(etats, mu_cible, label="Distribution cible")
plt.xlabel("Etat")
plt.ylabel("Proportion stationnaire")
plt.title("Comparaison des distributions")
plt.legend()
plt.tight_layout()
plt.savefig(fichier.parent / "comparaison_distributions.png")

# Sensibilite : on change la cible et on resout pour chaque epsilon.
epsilons = [0.05, 0.1, 0.25, 0.5, 0.75]
couts = []
nombres_modifies = []
for epsilon_test in epsilons:
    resultat_test = resoudre(epsilon_test)[0]
    modifications = resultat_test.x[m:2 * m] - resultat_test.x[2 * m:3 * m]
    nombre = np.count_nonzero(np.abs(modifications) > tolerance)
    couts.append(resultat_test.fun)
    nombres_modifies.append(nombre)
    print(f"Epsilon : {epsilon_test} | Cout : {resultat_test.fun:.4f} | Transitions modifiees : {nombre}")

plt.figure(figsize=(9, 3.2))

plt.subplot(1, 2, 1)
plt.plot(epsilons, couts, "o-")
plt.xlabel("Epsilon")
plt.ylabel("Somme des modifications")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(epsilons, nombres_modifies, "o-")
plt.xlabel("Epsilon")
plt.ylabel("Transitions modifiees")
plt.grid(True)

plt.tight_layout()
plt.savefig(fichier.parent / "sensibilite_rapport.png")
