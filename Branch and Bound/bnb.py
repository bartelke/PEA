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

    for i in range(1, nodesNumber):
        # stworzenie potomkow i obliczenie ich kosztu:
        if prev_mtx[prev_node][i] != -1:
            # lista potomkow:
            toVisit.append(i)
            # lista kosztow:
            cost = prev_cost + prev_mtx[0][i]
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

# dane z BnB [kolejny, minimum, macierz]
BnBresults = BnB(firstMTX, firstCost, nodesNumber, 0)

# odznacz miejsce:
matrixList.append(setRowsNColumns(BnBresults[2], 0, BnBresults[0]))
print(matrixList[1])


# print(toVisit)
# print(costList)
# print(local_min)
# print(next_node)

# # wybranie wierzcholka next_node i stworzenie dla niego macierzy:
# new_mtx = []
# # zaznaczenie przejscia w macierzy
# new_mtx = setRowsNColumns(prev_mtx, 0, next_node)
# minimalize(new_mtx)
# print(new_mtx)
# local_min = 9999999
# next_node = 0

# toVisit2 = []
# costList2 = []
# for i in range(1, nodesNumber):
#     prev_cost = 25

#     # stworzenie potomkow i obliczenie ich kosztu:
#     if new_mtx[3][i] != -1:
#         # lista potomkow:
#         toVisit2.append(i)
#         # lista kosztow:
#         cost = prev_cost + new_mtx[3][i]
#         costList2.append(cost)
#         if cost < local_min:
#             local_min = cost
#             next_node = i

# print(toVisit2)
# print(costList2)
# print(local_min)
# print(next_node)
