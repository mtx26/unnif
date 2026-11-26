from scipy.optimize import linprog
import numpy as np

# valeur d'entrée
G = np.array([
    [0.7, 0.3, 0.0],
    [0.0, 0.6, 0.4],
    [0.2, 0.0, 0.8]
])
epsilon = 0.1
mu = np.array([4 / 13, 3 / 13, 6 / 13])



n = G.shape[0]  # Nombre de lignes : ici 3
mu_cible = (1 - epsilon) * mu + epsilon * np.ones(n) / n

omega = []  # Au départ, aucune position enregistrée
# [(i, j) pour tous les i et j tels que G[i, j] > 0 ou i == j]
#exemple :
# [(0, 0), (0, 1), (1, 1), (1, 2), (2, 0), (2, 2)]  (exemple pour la matrice G donnée)
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


# Contrainte : T[i, j] - delta_plus[i, j] + delta_minus[i, j] - A[i, j] = -G[i, j] pour (i, j) dans omega
for k in range(m):
    i, j = omega[k]

    ligne = [0] * (6 * m)

    ligne[m + k] = 1 # delta +
    ligne[2 * m + k] = -1 # delta -
    ligne[3 * m + k] = -1 # A

    A_eq.append(ligne)
    b_eq.append(-G[i, j])


# Contrainte : somme des delta_plus et delta_moins pour chaque ligne i = 0
for i in range(n):
    ligne = [0] * (6 * m)

    for k in range(m):
        ligne_i, colonne_j = omega[k]

        if ligne_i == i:
            ligne[m + k] = 1 # delta +
            ligne[2 * m + k] = -1 # delta -

    A_eq.append(ligne)
    b_eq.append(0)


# Contrainte : somme des delta_plus et delta_moins pour chaque colonne j = 0
for j in range(n):
    ligne = [0] * (6 * m)

    for k in range(m):
        ligne_i, colonne_j = omega[k]

        if colonne_j == j:
            ligne[m + k] = mu_cible[ligne_i] # delta + pondéré par mu_cible[ligne_i]
            ligne[2 * m + k] = -mu_cible[ligne_i] # delta - pondéré par mu_cible[ligne_i]

    membre_droit = mu_cible[j] - sum(
        mu_cible[i] * G[i, j] for i in range(n) # Mu_cible * G , produit matriciel
    ) # mu - mu G

    A_eq.append(ligne)
    b_eq.append(membre_droit)


# Contrainte : T[i, j] - delta_plus[i, j] + delta_minus[i, j] - B[i, j] = 0 pour (i, j) dans omega
for i in range(n):
    for j in range(n):
        ligne = [0] * (6 * m)

        for k in range(m):
            ligne_i, colonne_j = omega[k]

            if ligne_i == i and colonne_j == j:
                ligne[k] = 1 # T
                ligne[m + k] = -1 # delta +
                ligne[2 * m + k] = 1 # delta -
                ligne[4 * m + k] = -1 # B


        A_eq.append(ligne)
        b_eq.append(0)

# Contrainte : T[i, j] - delta_plus[i, j] + delta_minus[i, j] - B[i, j] = 0 pour (i, j) dans omega (répétée pour chaque k)
for k in range(m):
    ligne = [0] * (6 * m)

    ligne[k] = 1
    ligne[m + k] = -1
    ligne[2 * m + k] = 1
    ligne[4 * m + k] = -1

    A_eq.append(ligne)
    b_eq.append(0)

# Contrainte : T[i, j] + delta_plus[i, j] - delta_minus[i, j] - C[i, j] = 0 pour (i, j) dans omega (répétée pour chaque k)
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

print("Valeur optimale :", resultat.fun)
print("G :")
print(G)
print("Delta :")
print(delta)
print("Matrice de transition modifiee G + Delta :")
print(G + delta)
print("Distribution initiale :", mu)
print("Distribution cible :", mu_cible)