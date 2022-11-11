from timeit import default_timer as timer


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

    return matrix, min


# wczytanie danych
path = "tsp_6_1.txt"
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

print(len(data))
print(minimalize(data))
