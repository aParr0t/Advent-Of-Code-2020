# read the input file
inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()

for i in range(len(puzzleInput)):
    puzzleInput[i] = puzzleInput[i].rstrip("\n")

bagTreeList = {}

for line in puzzleInput:
    # get parent bag
    parentBag = line[:line.index("contain")-6]

    # split each line into the different bag info
    childrenBags = list(line[line.index("contain")+8:-1].split(", "))
    for counter, string in enumerate(childrenBags):
        # get the count and name of the bag
        if "no other" in string:
            childName = None
            bagCount = None
        else:
            bagCount = int(string[:1])
            childName = string[2:string.index("bag")-1]

        # add the bag info to the array
        childrenBags[counter] = [childName, bagCount]
    bagTreeList[parentBag] = childrenBags


for key, value in bagTreeList.items():
    print(key, value)