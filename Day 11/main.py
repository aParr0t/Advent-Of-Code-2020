# read the input file
inputFile = open("input.txt", "r")
seats = inputFile.readlines()
for i in range(len(seats)):
    seats[i] = seats[i].rstrip("\n")

# This function is used for Part One
def adjacentNeighbours(i, j):
    neighbours = 0
    for y in range(j-1, j+2):
        for x in range(i-1, i+2):
            if x >= 0 and x < len(seats[0]) and y >= 0 and y < len(seats):
                if not(x == i and y == j):
                    if seats[y][x] == "#":
                        neighbours += 1
    return neighbours

def castRay(startX, startY, xVel, yVel):
    x, y = startX, startY
    while True:
        x += xVel
        y += yVel
        if x >= 0 and x < len(seats[0]) and y >= 0 and y < len(seats):
            if seats[y][x] == "#":
                return 1
            elif seats[y][x] == "L":
                return 0
        else:
            return 0


# This function is used for Part Two
def visibleNeighbours(i, j):
    neighbours = 0
    neighbours += castRay(i, j, -1, -1)
    neighbours += castRay(i, j, -1, 0)
    neighbours += castRay(i, j, -1, 1)
    neighbours += castRay(i, j, 0, -1)
    neighbours += castRay(i, j, 0, 1)
    neighbours += castRay(i, j, 1, -1)
    neighbours += castRay(i, j, 1, 0)
    neighbours += castRay(i, j, 1, 1)
    return neighbours


def applyRules(part):
    newSeats = []
    global seats
    for i in range(len(seats)):
        string = ""
        for j in range(len(seats[0])):
            if part == 1:
                neighbours = adjacentNeighbours(j, i)
            elif part == 2:
                neighbours = visibleNeighbours(j, i)

            if seats[i][j] == "L" and neighbours == 0:
                string += "#"
            elif seats[i][j] == "#" and neighbours >= 5:
                string += "L"
            else:
                string += seats[i][j]
            
        newSeats.append(string)
    return newSeats

roundCount = 0
newSeats = applyRules(2)
while seats != newSeats:
    seats = newSeats.copy()
    newSeats = applyRules(2)
    roundCount += 1
takenSeatCount = 0
for e in seats:
    takenSeatCount += e.count("#")
print("The answer for the chosen part: ", takenSeatCount)