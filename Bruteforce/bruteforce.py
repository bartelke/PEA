import itertools
from timeit import default_timer as timer

# wczytanie danych
data = []
with open("dane.txt") as f:
    # wczytanie ilosci wezlow (miast)
    nodesNumber = int(f.readline())

    for i in range(nodesNumber+1):
        singleData = [int(x) for x in f.readline().split()]
        data.append(singleData)

startTime = timer()
# lista miast ktora bedziemy permutowac
way = []
for i in range(1, nodesNumber):
    way.append(i)

# zbior wszystkich mozliwych sciezek (zbior wszystkich permutacji)
allPosibilities = list(itertools.permutations(way, nodesNumber-1))

# algorytm:
minCost = int(50000)

for i in range(len(allPosibilities)):  # <- sprawdzam po kolei permutacje
    # doliczenie dojscia z 0 do kolejnego wezla na poczatku i na koncu z ostatniego do 0
    begin = data[0][allPosibilities[i][0]]
    end = data[len(allPosibilities[i])][0]

    singleCost = int(begin + end)
    # sprawdzam koszt jednej sciezki
    for j in range(len(allPosibilities[i])-1):
        singleCost += (data[allPosibilities[i][j]][allPosibilities[i][j+1]])

    if (singleCost < minCost):
        minCost = singleCost

endTime = timer()
print("Min cost: " + str(minCost))
print(endTime-startTime)
