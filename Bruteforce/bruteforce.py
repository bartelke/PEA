import itertools

f = open("dane.txt", "r")
# wczytanie ilosci wezlow (miast)
nodesNumber = int(f.readline())

# lista miast ktora bedziemy permutowac
way = []
for i in range(1, nodesNumber):
    way.append(i)

print(way)
# zbior wszystkich mozliwych sciezek (zbior wszystkich permutacji)
allPosibilities = list(itertools.permutations(way, nodesNumber-1))

# dodanie wezla (miasta) poczatkowego i koncowego:
for i in range(len(allPosibilities)):
    singlePossibility = list(allPosibilities[i])
    singlePossibility.append(0)
    singlePossibility.insert(0, 0)
    allPosibilities[i] = singlePossibility

print(allPosibilities)
