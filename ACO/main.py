import math
import numpy
import networkx

from aco import ACO, Graph
import tsplib95


def loadData(file):
    global nodes
    global matrix
    global cities

    problemFile = tsplib95.load(file)
    graph = problemFile.get_graph()
    weight = networkx.to_numpy_array(graph)
    cities = list(problemFile.get_nodes())
    matrix = weight.tolist()
    print(matrix)


################################################################
# MAIN:
matrix = 0
cities = []
points = []
nodes = 0

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


rank = len(cities)

print(matrix)
aco = ACO(10, 100, 1.0, 10.0, 0.5, 10, 2)
graph = Graph(matrix, rank)
path, cost = aco.solve(graph)
print('cost: {}, path: {}'.format(cost, path))
