import sys
import tsplib95
from itertools import permutations
from itertools import combinations
from numpy import random
import numpy
import random
import copy
import time
import os
import psutil
import math


def loadGraph(file):
    global vertices
    global matrix
    matrix = tsplib95.load(file)
    vertices = list(matrix.get_nodes())


def simulatedAnnealing():
    global vertices
    global alpha
    global T_max
    global T_end
    global numEras

    currTemp = float(T_max)
    initPath = (numpy.array(vertices))
    random.shuffle(initPath)
    result = initPath.tolist()

    sameCost = 0
    acctepedWorse = 0

    while ((currTemp > T_end) and (sameCost < 15000) and (acctepedWorse < 15000)):
        for i in range(1, numEras + 1):
            neighbour = findNeighbour(result)
            resultCost = getCost(result)
            neighbourCost = getCost(neighbour)
            costDifference = neighbourCost - resultCost
            if (neighbourCost < resultCost):
                result = neighbour
                sameCost = 0
                acctepedWorse = 0
            else:
                s = random.random()
                p = math.exp(((-1 * float(costDifference)) / float(currTemp)))
                if (s < p):
                    if (costDifference == 0):
                        result = neighbour
                        sameCost += 1
                        acctepedWorse = 0

                    else:
                        result = neighbour
                        sameCost = 0
                        acctepedWorse += 1

            currTemp = (alpha ** i) * currTemp

    return result, getCost(result)


def findNeighbour(path):
    route = copy.deepcopy(path)
    neighbour = two_opt(route)
    return neighbour


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


if __name__ == "__main__":
    nodesNumber = 0
    csvFile = ""
    matrix = 0
    iterations = 0

    alpha = 0
    T_max = 0
    T_end = 0
    numEras = 0
    tspFile = ""
    with open("config.ini") as configFile:
        for line in configFile:
            pass
        csvFile = line

    with open("config.ini") as configFile:
        for line in configFile:
            line = line.split(' ')
            if (len(line) < 4):
                break

            tspFile = line[0]
            iterations = int(line[1])
            T_max = float(line[2])
            T_end = float(line[3])
            numEras = int(line[4])
            alpha = float(line[5])
            loadGraph(tspFile)
            startTime = time.time()
            resultPath, result = simulatedAnnealing()
            endTime = time.time()
            print("cost ", result)
            print('path ', resultPath)
            print('time ', endTime - startTime)
            print('memory', psutil.Process(
                os.getpid()).memory_info().rss / 1024 ** 2)
