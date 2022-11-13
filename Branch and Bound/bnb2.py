import math
from timeit import default_timer as timer


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

            # obliczanie ograniczenia dla pierwszego poziomu:
            if deepthLevel == 1:
                bound -= ((getMinimums(data,
                          currWay[deepthLevel - 1])[0] + getMinimums(data, i)[0])/2)
            # ograniczenie dla kolejnych poziomow:
            else:
                secondMin = getMinimums(data, currWay[deepthLevel - 1])[1]
                firstMin = getMinimums(data, i)[0]
                bound -= ((firstMin + secondMin)/2)

            # sprawdzenie czy powinnismy isc glebiej tym kierunkiem:
            if bound + actualCost < finalCost:
                # jesli tak to ustawiamy sprawdzany wezel na odwiedzony i dodajemy go do aktualnej sciezki
                # a nastepnie rekurencyjnie idziemy glebiej:
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

    # poczatkowa wartosc ograniczenia:
    bound = 0
    for i in range(N):
        bound += (getMinimums(data, i)[0] + getMinimums(data, i)[1])
    bound = math.ceil(bound / 2)

    rushToLeaf(data, bound, 0, 1, currWay, visitedNodes)


# wczytanie danych
iniFile = open("configuration.ini")

a = True

path = ""
maxsize = 999999999999
path = ""
loops = int(iniFile.readline())
while a:
    if not path:
        a = False

    path = iniFile.readline()
    print(path)
    data = []
    with open(path) as f:
        # wczytanie ilosci wiezlow (nodesNumber) oraz macierzy sasiedztwa(data):
        N = int(f.readline())

        for i in range(N + 1):
            singleData = [int(x) for x in f.readline().split()]
            data.append(singleData)

    resultsFile = open("results.txt", "a")
    resultsFile.write(
        "\n\n#########################\nNUMBER OF NODES: "+str(N)+"\n")
    # lp - iterator zliczajacy ile razy przeprowadzilismy badania dla danego grafu
    for lp in range(loops):
        startTime = timer()

        # ustawianie wartosci poczatkowych
        final_way = []
        visitedNodes = [False] * N
        finalCost = maxsize

        BnB(data)

        print("Koszt: ", finalCost)
        print("Sciezka: ", end=' ')
        print(final_way)
        endTime = timer()
        print(endTime-startTime)
        string = str("\nTime no." + str(lp) + ":     " +
                     str(endTime-startTime)+"  [s]")
        resultsFile.write(string)
        print(loops)
        print(path)
