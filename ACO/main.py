import math

from aco import ACO, Graph
import tsplib95


def loadData(file):
    global nodes
    global matrix
    matrix = tsplib95.load(file)
    nodes = len(list(matrix.get_nodes()))


################################################################
# MAIN:
matrix = 0
cities = []
points = []

# wczytywanie danych:
with open("config.ini") as configFile:
    for line in configFile:
        pass

    with open("config.ini") as configFile:
        for line in configFile:
            line = line.split(' ')
            if (len(line) < 5):
                print("zly plik ini")
                break

            pathToFile = line[0]
            loops = int(line[1])
            alpha = float(line[2])
            betha = float(line[3])
            trueResult = int(line[4])
            coolingMethod = int(line[5])

            print(alpha)

            loadData(pathToFile)

print(matrix)

with open('./data/chn31.txt') as f:
    for line in f.readlines():
        city = line.split(' ')
        cities.append(
            dict(index=int(city[0]), x=int(city[1]), y=int(city[2])))
        points.append((int(city[1]), int(city[2])))
cost_matrix = []

aco = ACO(10, 100, 1.0, 10.0, 0.5, 10, 2)
graph = Graph(matrix, nodes)
path, cost = aco.solve(graph)
print('cost: {}, path: {}'.format(cost, path))
