import tsplib95
import time
import copy
import random
import math

# wyzarzanie:


def annealing(initial_state, end_temp, initial_temp, temp_change, L):
    alpha = 1 - temp_change

    current_temp = initial_temp
    solution = initial_state
    same_solution = 0
    same_cost_diff = 0

    while current_temp > end_temp:
        for i in range(L):
            neighbor = get_neighbors(solution)

            # Oblicz roznice i sprawdz czy poprzednio znalezione rozwiazanie jest gorsze niz aktualne
            cost_diff = get_cost(neighbor) - get_cost(solution)
            if cost_diff > 0:
                solution = neighbor
                same_solution = 0
                same_cost_diff = 0

            elif cost_diff == 0:
                solution = neighbor
                same_solution = 0
                same_cost_diff += 1
            # jesli nowe rozwiazanie jest gorsze to zaakceptuj je z prawdopodobienstwem e^(-cost/temp)
            else:
                if random.uniform(0, 1) <= math.exp(float(cost_diff) / float(current_temp)):
                    solution = neighbor
                    same_solution = 0
                    same_cost_diff = 0
                else:
                    same_solution += 1
                    same_cost_diff += 1

            # chlodzenie
            current_temp = current_temp*alpha

    return solution, 1/get_cost(solution)


def get_cost(state):
    """Calculates cost/fitness for the solution/route."""
    distance = 0

    for i in range(len(state)):
        from_city = state[i]
        to_city = None
        if i+1 < len(state):
            to_city = state[i+1]
        else:
            to_city = state[0]
        distance += data.get_weight(from_city, to_city)
    fitness = 1/float(distance)
    return fitness


def get_neighbors(state):
    """Returns neighbor of  your solution."""

    neighbor = copy.deepcopy(state)
    swap(neighbor)

    return neighbor


def swap(state):
    "Swap cities at positions i and j with each other"
    pos_one = random.choice(range(len(state)))
    pos_two = random.choice(range(len(state)))
    state[pos_one], state[pos_two] = state[pos_two], state[pos_one]

    return state


###########################################################
# MAIN:
best_route_distance = []
best_route = []
convergence_time = []

# wczytanie danych
iniFile = open("configuration.ini")
path = ""
loops = int(iniFile.readline())
initial_temp = float(iniFile.readline())
temp_change = float(iniFile.readline())
end_temp = float(iniFile.readline())
L = int(iniFile.readline())
path = iniFile.readline()

# wczytanie plikow z tsplib
data = tsplib95.load(path)
first_route = list(data.get_nodes())

# losowe poczatkowe rozwiazanie:
random.shuffle(first_route)

resultsFile = open("results.csv", "a")
resultsFile.write("\n#############################################\n")

for i in range(loops):
    # pojedyncze wykonanie algorytmu:
    start = time.time()
    route, route_distance = annealing(
        first_route, end_temp, initial_temp, temp_change, L)
    time_elapsed = time.time() - start
    best_route_distance.append(route_distance)
    best_route.append(route)
    convergence_time.append(time_elapsed)

    print(best_route_distance)
    print(best_route)
    print(convergence_time)

    # zapis wynikow do pliku:
    resultsFile.write(str(path) + ", " + str(route_distance) + ", " + str(time_elapsed) + ", " +
                      str(initial_temp) + ", " + str(temp_change) + ", " + str(L) + "\n")
