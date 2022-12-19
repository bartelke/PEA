import tsplib95
import numpy
import random
import copy
import time
import math


def simulatedAnnealing():
    global nodes
    global T_start
    global T_stop
    global L
    global alpha

    currTemp = float(T_start)
    initPath = (numpy.array(nodes))
    random.shuffle(initPath)
    result = initPath.tolist()

    sameCost = 0
    numOfWorseAcc = 0

    while ((currTemp > T_stop) and (sameCost < 15000) and (numOfWorseAcc < 15000)):
        # L = dlugosc epoki
        for i in range(1, L + 1):
            neighbour = findNeighbour(result)
            resultCost = getCost(result)
            neighbourCost = getCost(neighbour)
            diff = neighbourCost - resultCost
            if (neighbourCost < resultCost):
                # przyjęcie lepszego wyniku
                result = neighbour
                sameCost = 0
                numOfWorseAcc = 0
            else:
                # prawdopodobieństwo do przyjęcia gorszego wyniku
                s = random.random()
                p = math.exp(((-1 * float(diff)) / float(currTemp)))
                if (s < p):
                    if (diff == 0):
                        result = neighbour
                        sameCost += 1
                        numOfWorseAcc = 0

                    else:
                        # przyjecie gorszego wyniku
                        result = neighbour
                        sameCost = 0
                        numOfWorseAcc += 1

            # chłodzenie
            currTemp = (alpha ** i) * currTemp

    return result, getCost(result)


def findNeighbour(path):
    route = copy.deepcopy(path)
    neighbour = two_opt(route)
    return neighbour


# 2-zamiana:
def two_opt(path):
    pathLength = len(path)
    v1 = random.choice(path)
    v2 = random.choice(path)
    if (v1 == v2):
        while (v1 == v2):
            v1 = random.choice(path)
            v2 = random.choice(path)

    if (v1 > v2):
        firstPath = path[0: v2]
        reversePath = path[v2: v1][::-1]
        lastPath = path[v1:pathLength]
        neighbour = firstPath + reversePath + lastPath
    else:
        firstPath = path[0: v1]
        reversePath = path[v1: v2][::-1]
        lastPath = path[v2: pathLength]
        neighbour = firstPath + reversePath + lastPath

    return neighbour


def getCost(path):
    global matrix
    cost = 0
    for i in range(0, len(path)):
        if (i + 1 < len(path)):
            destination = path[i + 1]
        else:
            destination = path[0]
        cost += matrix.get_weight(path[i], destination)
    return cost


def loadData(file):
    global nodes
    global matrix
    matrix = tsplib95.load(file)
    nodes = list(matrix.get_nodes())


############################################
# MAIN:
matrix = 0
loops = 0

alpha = 0
T_start = 0
T_stop = 0
L = 0
pathToFile = ""
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
            T_start = float(line[2])
            T_stop = float(line[3])
            L = int(line[4])
            alpha = float(line[5])
            trueResult = int(line[6])

            loadData(pathToFile)

           # pomiary:
            startTime = time.time()
            resultRoute, result = simulatedAnnealing()
            endTime = time.time()
            totalTime = round(endTime - startTime, 3)

            print("cost ", result)
            print('path ', resultRoute)
            print('time ', totalTime)
            differencePertentage = round(
                abs(trueResult-result)*100/trueResult, 2)
            print(str(differencePertentage) + "% ")

        # zapis wynikow do pliku:
        resultsFile = open("results.csv", "a")
        resultsFile.write("\n\n")
        resultsFile.write(str(pathToFile) + ", " + str(result) + ", " + str(totalTime) + ", " +
                          str(T_start) + ", " + str(alpha) + ", " + str(L) + ", " + str(differencePertentage) + "% \n")
