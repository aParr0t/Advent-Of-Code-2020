import time
start_time = time.time()

# read the input file
inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()
for i in range(len(puzzleInput)):
    puzzleInput[i] = puzzleInput[i].rstrip("\n")


# # Part One
# busses = [int(x) for x in puzzleInput[1].split(",") if x != "x"]
# earliestTime = int(puzzleInput[0])
# lowestBusTime = 999999999999
# lowestBus = 0

# for e in busses:
#     busTime = (earliestTime//e + 1)*e
#     if busTime < lowestBusTime:
#         lowestBusTime = busTime
#         lowestBus = e
# print("Part One answer : ", (lowestBusTime - earliestTime) * lowestBus)
# # Part One


# Part Two
# My sollution - aka brute force
# delays = []
# busses = [x for x in puzzleInput[1].split(",")]
# for idx, item in enumerate(busses):
#     if item != "x":
#         delays.append(idx)
# busses = [int(x) for x in puzzleInput[1].split(",") if x != "x"]
# highestBusID = max(busses)
# highestBusDelay = puzzleInput[1].split(",").index(str(highestBusID))

# def testDeparture(time):
#     for i in range(len(busses)):
#         if ((time + delays[i]) % busses[i]) != 0:
#             return False
#     return True


# t = (100000000000000//highestBusID) * highestBusID
# print(t)
# while True:
#     t += highestBusID
#     if testDeparture(t-highestBusDelay):
#         print("Part Two answer : ", t-highestBusDelay)
#         break

# # 1202161486
# # 100000000000000
# # 11546953709433246720
# print("--- %s seconds ---" % (time.time() - start_time))

# Part Two
# Chinese remainder theorem

def modularInverse(a, m):
    x, y = a, m
    while x-1 != y:
        x += a
        if x-y > 1:
            y += m
    return x//a
print(modularInverse(10, 17))