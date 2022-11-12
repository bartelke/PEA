from timeit import default_timer as timer
import copy


def setRowsNColumns(mtx, row, col):
    matrix = mtx
    matrix[row][col] = -1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == row or j == col:
                matrix[i][j] = -1
    return matrix


def BnB(prev_mtx, prev_cost, nodesNumber, prev_node):
    toVisit = []
    costList = []
    local_min = 99999999
    next_node = 0

    for i in range(1, nodesNumber):
        # stworzenie potomkow i obliczenie ich kosztu:
        element = int(prev_mtx[prev_node][i])
        if element != -1:
            # lista potomkow:
            toVisit.append(i)
            # lista kosztow:
            cost = prev_cost + element
            costList.append(cost)
            if cost < local_min:
                local_min = cost
                next_node = i

    results = [next_node, local_min, prev_mtx]
    return results


def minimalize(matrix):
    cost = 0

    # minimalizacja po wierszach:
    for i in range(len(matrix)):
        j = 0
        min = 99999999
        should_minimalize = False

        while matrix[i][j] != 0:
            # wartosc minimalna:
            if matrix[i][j] < min and matrix[i][j] > -1:
                min = matrix[i][j]

            j += 1
            if j == len(matrix):
                should_minimalize = True
                break
        # wlasciwa czesc redukcji:
        if should_minimalize == True:
            cost += min
            for j in range(len(matrix)):
                if matrix[i][j] != -1:
                    matrix[i][j] = matrix[i][j] - min

    # minimalizacja po kolumnach:
    for i in range(len(matrix)):
        j = 0
        min = 99999999
        should_minimalize = False

        while matrix[j][i] != 0:
            # wartosc minimalna:
            if matrix[j][i] < min and matrix[j][i] > -1:
                min = matrix[j][i]

            j += 1
            if j == len(matrix):
                should_minimalize = True
                break
        # wlasciwa czesc redukcji:
        if should_minimalize == True:
            cost += min
            for j in range(len(matrix)):
                if matrix[j][i] != -1:
                    matrix[j][i] = matrix[j][i] - min

    res = [matrix, cost]
    return res


# wczytanie danych
path = "hindutest.txt"
data = []
with open(path) as f:
    # wczytanie ilosci wiezlow (nodesNumber) oraz macierzy sasiedztwa(data):
    nodesNumber = int(f.readline())

    for i in range(nodesNumber):
        singleData = [int(x) for x in f.readline().split()]
        data.append(singleData)

# zmiana 0 na -1 do obliczen:
for i in range(nodesNumber):
    for j in range(nodesNumber):
        if i == j:
            data[i][j] = -1

# pierwszy wezel:
matrixList = []
matrixList.append(minimalize(copy.deepcopy(data)))

firstMTX = matrixList[0][0]
firstCost = matrixList[0][1]

#######################################################
# uwaga!!! element o indeksie 0 ma inny typ niz pozostale na matrixList dlatego zaczynamy od 1
index = 1
matrixList.append(firstMTX)
prevNode = 0
cost = int(firstCost)


way = [0]
while len(way) < nodesNumber:
    # dane z BnB [kolejny, minimum, macierz] (podaj: macierz poprzedniego wierzcholka, jego koszt, nodesNumber i ktory to wierzcholek)
    BnBresults = BnB(matrixList[index], cost, nodesNumber, prevNode)

    # odznacz miejsce:
    matrixList.append(setRowsNColumns(
        BnBresults[2], prevNode, BnBresults[0]))
    prevNode = BnBresults[0]

    cost = BnBresults[1]
    way.append(BnBresults[0])

way.append(0)
print(way)