from timeit import default_timer as timer

# wczytanie danych
path = "tsp_6_1.txt"
data = []
with open(path) as f:
    # wczytanie ilosci wiezlow (nodesNumber) oraz macierzy sasiedztwa(data):
    nodesNumber = int(f.readline())

    for i in range(nodesNumber):
        singleData = [int(x) for x in f.readline().split()]
        data.append(singleData)

print(data)
