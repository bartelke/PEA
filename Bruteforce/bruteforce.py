import itertools

f = open("dane.txt", "r")
# wczytanie ilosci wezlow (miast)
nodesNumber = int(f.readline())

# lista miast ktora bedziemy permutowac
way = []
for i in range(1, nodesNumber):
    way.append(i)

# zbior wszystkich mozliwych sciezek (zbior wszystkich permutacji)
allPosibilities = list(itertools.permutations(way, nodesNumber-1))

# dodanie wezla (miasta) poczatkowego i koncowego:
for i in range(len(allPosibilities)):
    singlePossibility = list(allPosibilities[i])
    singlePossibility.append(0)
    singlePossibility.insert(0, 0)
    allPosibilities[i] = singlePossibility

# wczytanie danych
data = []
with open("dane.txt") as f:
    for i in range(nodesNumber+1):
        singleData = [int(x) for x in f.readline().split()]
        data.append(singleData)
data.pop(0)

# algorytm:
minCost = int(50000)


for i in range(len(allPosibilities)):  # <- sprawdzam po kolei permutacje
    singleCost = int(0)
    # sprawdzam koszt jednej sciezki
    for j in range(len(allPosibilities[i])-1):
        singleCost += (data[allPosibilities[i][j]][allPosibilities[i][j+1]])
        # print(singleCost)

if (singleCost < minCost):
    minCost = singleCost

print("Min cost: " + str(minCost))
