import random
import sys
import time
from datetime import datetime
from queue import Queue
from queue import PriorityQueue

N = 1000 # map size
sys.setrecursionlimit(N*N+5) # this function only works in newer versions of Python. If it's not working, lower the value of N. 

def randSquare(): # from the given part 2 solution
    Pr_normal = 0.4
    Pr_forest = 0.4
    Pr_mountain = 0.2
    probs = [Pr_normal, Pr_forest, Pr_mountain]
    return random.choices(['.','F','X'],weights=probs, k=1)[0]

def initRainGrid(): # set up the rain for the first time
    Pr_Rain = 0.4
    for i in range(N):
        rainMatrix[i] = random.choices([0,1], weights=[1-Pr_Rain,Pr_Rain], k=N)

def genNewRain(): # when new rain is generated, returns a list of where the rain is happening. Also updates the rainMatrix.
    numRain = random.randint(0, 20) # change the amount of rain
    rainUpdates = []
    for i in range(numRain):
        updateI = random.randint(0, N-1)
        updateJ = random.randint(0, N-1)
        rainUpdates.append((updateI, updateJ))
        rainMatrix[updateI][updateJ] = 1-rainMatrix[updateI][updateJ]
    return rainUpdates

def dfs(i, j, label): # connectivity DFS
    connectedMatrix[i][j] = label
    if i > 0 and grid[i-1][j] != 'X' and connectedMatrix[i-1][j] == 0:
        dfs(i-1, j, label) # go left
    if i < N-1 and grid[i+1][j] != 'X' and connectedMatrix[i+1][j] == 0:
        dfs(i+1, j, label) # go right
    if j > 0 and grid[i][j-1] != 'X' and connectedMatrix[i][j-1] == 0:
        dfs(i, j-1, label) # go up
    if j < N-1 and grid[i][j+1] != 'X' and connectedMatrix[i][j+1] == 0:
        dfs(i, j+1, label) # go down

def updateRain(curI, curJ, endI, endJ, currentOptimal): # returns whether or not a recalculation should happen
    rainUpdates = genNewRain()
    for coordinate in rainUpdates:
        i = coordinate[0]
        j = coordinate[1]
        if coordinate in nextMovesSet:
            if rainMatrix[i][j] == 1: # rain was added to the current path
                return True
        elif rainMatrix[i][j] == 0 and grid[i][j] != 'X' and mhDistance(curI, curJ, i, j)+mhDistance(i, j, endI, endJ)<currentOptimal: # rain was removed
                return True
    return False

def mhDistance(i, j, ei, ej): # manhattan distance between two squares
    return abs(ei-i)+abs(ej-j)

def tryMove(currentDistance, distanceMatrix, i, j): # check whether it is optimal to move there for A*
    if not validate(i) or not validate(j) or grid[i][j] == 'X': # illegal move
        return -1
    
    newDistance = 0 # finding the cost to move to i, j
    if grid[i][j] == '.':
        newDistance = 1
    else:
        newDistance = 2

    if rainMatrix[i][j]:
        newDistance = newDistance*2

    newDistance += currentDistance
    if distanceMatrix[i][j] == -1 or newDistance < distanceMatrix[i][j]: # this move is an improvement
        return newDistance # we should move
    return -1 # we shouldn't move


def answerQuery(startI, startJ, endI, endJ): # runs A* and finds the path
    start_time = time.time() # debug
    
    while not nextMoves.empty(): # clearing old values
        nextMoves.get()
    nextMovesSet.clear()
    
    pq = PriorityQueue()
    curCoordinate = (startI, startJ)
    distanceMatrix[startI][startJ] = 0
    pq.put((mhDistance(startI, startJ, endI, endJ), curCoordinate))

    updatedSquares = {(startI, startJ)} # keeping track of all squares updated

    while pq.qsize() > 0:
        coordinate = pq.get() # returns value and also pops
        i = coordinate[1][0]
        j = coordinate[1][1]
        currentDistance = distanceMatrix[i][j]
        if i == endI and j == endJ: # early exit, we're at the end
            break

        temp = tryMove(currentDistance, distanceMatrix, i-1, j)
        if temp > 0:
            backtrack[i-1][j] = (i, j)
            distanceMatrix[i-1][j] = temp
            updatedSquares.add((i-1, j))
            pq.put((temp+mhDistance(i-1, j, endI, endJ), (i-1, j)))
            
        temp = tryMove(currentDistance, distanceMatrix, i+1, j)
        if temp > 0:
            backtrack[i+1][j] = (i, j)
            distanceMatrix[i+1][j] = temp
            updatedSquares.add((i+1, j))
            pq.put((temp+mhDistance(i+1, j, endI, endJ), (i+1, j)))

        temp = tryMove(currentDistance, distanceMatrix, i, j-1)
        if temp > 0:
            backtrack[i][j-1] = (i, j)
            distanceMatrix[i][j-1] = temp
            updatedSquares.add((i, j-1))
            pq.put((temp+mhDistance(i, j-1, endI, endJ), (i, j-1)))
        
        temp = tryMove(currentDistance, distanceMatrix, i, j+1)
        if temp > 0:
            backtrack[i][j+1] = (i, j)
            distanceMatrix[i][j+1] = temp
            updatedSquares.add((i, j+1))
            pq.put((temp+mhDistance(i, j+1, endI, endJ), (i, j+1)))

    i = endI # beginning our backtrack at the end square
    j = endJ
    moves = [] #stack
    while backtrack[i][j] != (-1, -1): # keeping going backwards until we reach the first square...
        # ...which backtrack didn't set so it's the default value of (-1, -1).
        coordinate = (i, j)
        moves.append(coordinate) # put into stack
        tempI = i
        tempJ = j
        i = backtrack[tempI][tempJ][0] # move backwards one square
        j = backtrack[tempI][tempJ][1]
    while len(moves)>0:
        nextMoves.put(moves[-1]) # put the top element of the stack into nextMoves, essentially reversing its order
        nextMovesSet.add(moves[-1])
        moves.pop()
    print(f"explored {len(updatedSquares)}") # debug
    for coordinate in updatedSquares: # clearing all values
        backtrack[coordinate[0]][coordinate[1]] = (-1, -1)
        distanceMatrix[coordinate[0]][coordinate[1]] = -1
    
    # below: debug stats
    end_time = time.time()
    global_stats[0] += 1
    global_stats[1] += end_time - start_time
    return distanceMatrix[endI][endJ] # returning so currentDistance can be updated in the while True loop

def moveCost(top): # function to quickly find out cost of moving one step
    t = 0
    if grid[top[0]][top[1]] == 'F':
        t = 2
    else:
        t = 1
    if rainMatrix[top[0]][top[1]] == 1:
        t *= 2
    return t
   
def validate(coord): # checking bounds
    if coord < 0 or coord >= N:
        return False
    else:
        return True

grid = []
for i in range(N):
    grid.append([randSquare() for j in range(N)])

for i in range(N):
    print(grid[i])

connectedMatrix = []
for i in range(N):
    connectedMatrix.append([0 for j in range(N)])

rainMatrix = []
for i in range(N):
    rainMatrix.append([])
initRainGrid() # populating grid with rain initially
for i in range(N):
   print(rainMatrix[i])

distanceMatrix = []
for i in range(N):
    distanceMatrix.append([-1 for j in range(N)])

nextMoves = Queue()
nextMovesSet = set()

backtrack = []
for i in range(N):
    backtrack.append([(-1, -1) for j in range(N)])
# end of setup


label = 1
for i in range(N):
    for j in range(N):
        if connectedMatrix[i][j] == 0 and grid[i][j] != 'X': # don't set squares that have already been processed
            dfs(i, j, label) # doing the connected matrix
            label += 1 # different label for each connected component
print()
for i in range(N):
    print(connectedMatrix[i])

# end of connectivity check

global_stats = [0, 0, 0] # for debug: number of answerQuery calls, total answerQuery time in seconds, average answerQuery time

print("coordinates in startI, startJ, endI, endJ format, with top left as (0, 0)")

while True:
    inStr = input("type q to finish, enter 4 coordinates: ")
    if len(inStr) == 0:
        continue
    elif inStr == 'q' or inStr == 'Q':
        print("it didn't crash yay")
        exit(0)
    else: 
        try:
            startI, startJ, endI, endJ = map(int, inStr.split())
        except Exception as e:
            print("4 coords with spaces in between:")
            continue
            
        if not (validate(startI) and validate(startJ) and validate(endI) and validate(endJ)):
            print("coord(s) out of range")
            continue
    
    # below: debug stats
    global_stats = [0, 0, 0]
    global_start_time = datetime.now()
    actualLength = 0
    totalQueries = 1

    # below: algorithm
    if startI == endI and startJ == endJ:
        print("same square")
        continue
    if grid[startI][startJ] == 'X' or grid[endI][endJ] == 'X':
        print("no path (start/end is mountain)")
        continue
    if (connectedMatrix[startI][startJ] != connectedMatrix[endI][endJ]):
        print("no path")
        continue
    
    currentDist = answerQuery(startI, startJ, endI, endJ) # finds a current best solution based on the rain
    while nextMoves.qsize() > 0: # while there are still moves left (ie: not at the end yet)
        top = nextMoves.get() # this is point where in griddo, the player would actually move
        actualLength += moveCost(top) 
        currentDist -= moveCost(top) # changing the current optimal upper bound
        if updateRain(top[0], top[1], endI, endJ, currentDist) == True: # updates the rain and then checks if a recalculation needs to happen
            currentDist = answerQuery(top[0], top[1], endI, endJ) # reupdating if it's needed
        else:
            print("recalc skipped") # debug
        print(f"moved altogether {actualLength}") # debug

    # below: all debug
    print(f"reached - start time: {global_start_time}; end time: {datetime.now()}")
    global_stats[2] = global_stats[1] / global_stats[0]
    print(f"Number of path calculations: {global_stats[0]}; Total path calculation time (s): {global_stats[1]:.1f}; Average path calculation (s): {global_stats[2]:.1f}")

