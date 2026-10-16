import random
import time
from concurrent.futures import ThreadPoolExecutor


class TSP:

    def __init__(self, tsp=None):
        if tsp is None:
            tsp = [[]]
        self.tsp = tsp

    def get_cout(self, ville1, ville2):
        return self.tsp[ville1 - 1][ville2 - 1]

    def total_cout(self, villes):
        c = 0

        for i in range(len(villes) - 1):
            c += self.get_cout(villes[i], villes[i + 1])

        return c

    @staticmethod
    def get_random_TSP(n=2):
        tsp = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

        for i in range(n):
            tsp[i][i] = 0

        return TSP(tsp)

    def TSPSolver(self):
        villes = list(range(1, len(self.tsp) + 1))
        best_route = None
        best_cost = float("inf")

        for route in routes(villes):
            route_complete = route + [route[0]]
            cost = self.total_cout(route_complete)

            if cost < best_cost:
                best_cost = cost
                best_route = route_complete

        return best_route, best_cost

    def greedySolver(self, start=1):
        n = len(self.tsp)

        route = [start]
        non_visitees = list(range(1, n + 1))
        non_visitees.remove(start)

        ville_actuelle = start

        while len(non_visitees) > 0:
            meilleure_ville = None
            meilleur_cout = float("inf")

            for ville in non_visitees:
                cout = self.get_cout(ville_actuelle, ville)

                if cout < meilleur_cout:
                    meilleur_cout = cout
                    meilleure_ville = ville

            route.append(meilleure_ville)
            non_visitees.remove(meilleure_ville)
            ville_actuelle = meilleure_ville

        route_complete = route + [start]
        return route_complete, self.total_cout(route_complete)

    def dynamicSolver(self, start=1):
        villes = list(range(1, len(self.tsp) + 1))
        restantes = villes.copy()
        restantes.remove(start)

        memo = {}

        return self._dynamic(start, restantes, start, memo)

    def _dynamic(self, current, restantes, start, memo):
        key = (current, tuple(sorted(restantes)))

        if key in memo:
            return memo[key]

        if len(restantes) == 0:
            result = ([current, start], self.get_cout(current, start))
            memo[key] = result
            return result

        best_route = None
        best_cost = float("inf")

        for ville in restantes:
            nouvelles_restantes = restantes.copy()
            nouvelles_restantes.remove(ville)

            route, cost = self._dynamic(ville, nouvelles_restantes, start, memo)
            total = self.get_cout(current, ville) + cost

            if total < best_cost:
                best_cost = total
                best_route = [current] + route

        result = (best_route, best_cost)
        memo[key] = result
        return result


def routes(villes):
    if len(villes) == 1:
        yield villes
        return

    for i in range(len(villes)):
        ville = villes[i]
        restantes = villes[:i] + villes[i + 1:]

        for route in routes(restantes):
            yield [ville] + route


def mesure_temps(nom, fonction):
    debut = time.perf_counter()
    route, cout = fonction()
    fin = time.perf_counter()

    return nom, route, cout, fin - debut


def comparer_solveurs(tsp):
    solveurs = [
        ("Brute force", tsp.TSPSolver),
        ("Glouton", tsp.greedySolver),
        ("Dynamique", tsp.dynamicSolver)
    ]

    with ThreadPoolExecutor() as executor:
        futures = []

        for nom, fonction in solveurs:
            futures.append(executor.submit(mesure_temps, nom, fonction))

        for future in futures:
            nom, route, cout, temps = future.result()

            print("-----", nom, "-----")
            print("Route :", route)
            print("Coût :", cout)
            print("Temps :", temps, "secondes")
            print()


tsp = TSP([
    [0, 4, 7],
    [7, 0, 5],
    [3, 2, 0]
])

tsp2 = TSP.get_random_TSP(10)

print("Petit TSP :")
comparer_solveurs(tsp)

print("Grand TSP :")
comparer_solveurs(tsp2)