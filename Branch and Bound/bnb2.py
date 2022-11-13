import math


def getMinimums(data, i):
    firstMinVal = maxsize
    secondMinVal = maxsize

    for j in range(N):
        if i == j:
            continue
        if data[i][j] <= firstMinVal:
            secondMinVal = firstMinVal
            firstMinVal = data[i][j]

        elif (data[i][j] <= secondMinVal and
              data[i][j] != firstMinVal):
            secondMinVal = data[i][j]

    results = [firstMinVal, secondMinVal]
    return results


# funkcja zajmujaca sie pojedyncza sciezka (dotarciem do jakiegos liscia):
def rushToLeaf(data, bound, actualCost, deepthLevel, currWay, visitedNodes):
    global finalCost

    for i in range(N):
        # sprawdzenie czy dany wiezcholek nie byl jeszcze odwiedzony lub czy nie jest to petla:
        if (visitedNodes[i] == False) and (data[currWay[deepthLevel-1]][i] != 0):
            boundCopy = bound
            actualCost += data[currWay[deepthLevel - 1]][i]

            # obliczanie ograniczenia:
            if deepthLevel == 1:
                bound -= ((getMinimums(data,
                          currWay[deepthLevel - 1])[0] + getMinimums(data, i)[0])/2)
            else:
                secondMin = getMinimums(data, currWay[deepthLevel - 1])[1]
                firstMin = getMinimums(data, i)[0]
                bound -= ((firstMin + secondMin)/2)

            # sprawdzenie czy powinnismy isc glebiej tym kierunkiem:
            if bound + actualCost < finalCost:
                # jesli tak to ustawiamy sprawdzany wezel na odwiedzony i dodajemy go do aktualnej sciezki
                # a nastepnie rekurencyjnie idziemy glebiej az do liscia:
                visitedNodes[i] = True
                currWay[deepthLevel] = i

                rushToLeaf(data, bound, actualCost,
                           deepthLevel + 1, currWay, visitedNodes)

            # gdy przekroczymy granice to ucinamy ta sciezke:
            actualCost -= data[currWay[deepthLevel - 1]][i]
            bound = boundCopy
            visitedNodes = [False] * len(visitedNodes)
            for j in range(deepthLevel):
                if currWay[j] != -1:
                    visitedNodes[currWay[j]] = True

    # warunek koncowy jesli dotrzemy do liscia:
    if deepthLevel == N:

        penVertex = data[currWay[deepthLevel - 1]][currWay[0]]
        if penVertex != 0:
            # koszt obecnie sprawdzonej sciezki (calej)
            currentCost = actualCost + penVertex

            # sprawdzenie czy aktualnie wyliczony koszt jest mniejszy niz dotychczas znalezione minimum:
            if currentCost < finalCost:
                final_way[:N + 1] = currWay[:]
                final_way[N] = currWay[0]
                finalCost = currentCost
        return


def BnB(data):
    # pojedyncza sprawdzana sciezka:
    currWay = [-1] * (N + 1)
    currWay[0] = 0

    # lista odwiedzonych wierzcholkow:
    visitedNodes = [False] * N
    visitedNodes[0] = True

    # granica:
    bound = 0
    for i in range(N):
        bound += (getMinimums(data, i)[0] + getMinimums(data, i)[1])
    bound = math.ceil(bound / 2)

    rushToLeaf(data, bound, 0, 1, currWay, visitedNodes)


maxsize = 999999999999
path = "tsp_12.txt"
data = []
with open(path) as f:
    # wczytanie ilosci wiezlow (nodesNumber) oraz macierzy sasiedztwa(data):
    N = int(f.readline())

    for i in range(N):
        singleData = [int(x) for x in f.readline().split()]
        data.append(singleData)

final_way = []
visitedNodes = [False] * N
finalCost = maxsize

BnB(data)

print("Koszt: ", finalCost)
print("Sciezka: ", end=' ')
print(final_way)
