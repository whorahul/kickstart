t = int(input())


def preprocess(n,m,A):
    connections = {}
    for i in range(n):
        for j in range(m):
            if A[i][j] == "#":
                continue
            north = i
            south = i
            east = j
            west = j
            while north > -1 and A[north][j] != "#":
                north -= 1
            while south < n and A[south][j] != "#":
                south += 1
            while east < m  and A[i][east] != "#":
                east += 1
            while west > -1 and A[i][west] != "#":
                west -= 1
            # want i - north = south - complement, so complement = south + north -i
            if south + north == 2*i and east + west == 2*j:
                continue
            connections[(i,j)] = []
            if south + north != 2*i:
                connections[(i,j)].append((south + north -i,j))
            if east + west != 2*j:
                connections[(i,j)].append((i, east + west - j))
    return connections

def getAnswer(n,m, A_old):
    A = [[element for element in row] for row in A_old]
    connections = preprocess(n,m,A)
    starters = set(filter(lambda x: A[x[0]][x[1]] != ".", connections.keys()))
    checked = set()
    numFilled = 0
    while starters != set():
        randomElement = starters.pop()
        toCheck = [randomElement]
        while toCheck != []:
            top = toCheck.pop()
            neighbors = connections[top]
            checked.add(top)
            for neighbor in neighbors:
                if neighbor not in checked:
                    if A[neighbor[0]][neighbor[1]] == ".":
                        A[neighbor[0]][neighbor[1]] = A[top[0]][top[1]]
                        numFilled += 1
                        toCheck.append(neighbor)
    return numFilled, A

def printGrid(grid):
    for column in grid:
        print("".join(column))


for case in range(1, t+1):
    L1 = [int(n) for n in input().split()]
    n, m = L1
    A = [list(input()) for i in range(n)]
    
    numFilled, grid = getAnswer(n,m, A)
    print("Case #%s: %s" % (case, numFilled))
    printGrid(grid)
