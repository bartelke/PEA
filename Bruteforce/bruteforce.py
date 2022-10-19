import itertools
from timeit import default_timer as timer

# wczytanie danych
iniFile = open("configuration.ini")

a = True

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
        nodesNumber = int(f.readline())

        for i in range(nodesNumber+1):
            singleData = [int(x) for x in f.readline().split()]
            data.append(singleData)

    resultsFile = open("results.txt", "a")
    resultsFile.write(
        "\n\n#########################\nNUMBER OF NODES: "+str(nodesNumber)+"\n")

    # lp - iterator zliczajacy ile razy przeprowadzilismy badania dla danego grafu
    for lp in range(loops):

        startTime = timer()
        # lista wierzcholkow ktore bedziemy permutowac:
        nodes = []
        for i in range(1, nodesNumber):
            nodes.append(i)

        # zbior wszystkich mozliwych sciezek (zbior wszystkich permutacji)
        allPosibilities = list(itertools.permutations(nodes, nodesNumber-1))

        # tu zaczyna sie algorytm:
        minCost = int(5000000)

        for i in range(len(allPosibilities)):  # <- sprawdzam po kolei permutacje
            # doliczenie dojscia z 0 do kolejnego wezla na poczatku i na koncu z ostatniego do 0
            begin = data[0][allPosibilities[i][0]]
            end = data[len(allPosibilities[i])][0]

            singleCost = int(begin + end)
            # petla obliczajaca koszt jednej sciezki
            for j in range(len(allPosibilities[i])-1):
                singleCost += (data[allPosibilities[i][j]]
                               [allPosibilities[i][j+1]])

            if (singleCost < minCost):
                minCost = singleCost

        endTime = timer()
        print("Min cost: " + str(minCost))
        print(endTime-startTime)
        string = str("\nTime no." + str(lp) + ":     " +
                     str(endTime-startTime)+"  [s]")
        resultsFile.write(string)
        print(loops)
        print(path)
