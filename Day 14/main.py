# read the input file
inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()
for i in range(len(puzzleInput)):
    puzzleInput[i] = puzzleInput[i].rstrip("\n")

# Part One
mem = {}
mask = ""
for line in puzzleInput:
    if "ma" in line:
        # set the mask
        mask = list(line[7:])
    else:   
        # convert the int to binary and split the binary num into a list
        num = list('{0:036b}'.format(int(line[line.index("=")+2:])))
        # set the mask on the binary number list
        for i in range(len(mask)):
            if mask[i] != "X":
                num[i] = mask[i]
        # convert the binary num list back to a num and save it to memory
        mem[line[4:line.index("]")]] = int("".join(num), 2)

print("Part One answer : ", sum(mem.values()))
# Part One



# Part Two
mem = {}
mask = ""
for line in puzzleInput:
    if "ma" in line:
        # set the mask
        mask = list(line[7:])
    else:   
        # convert the int to binary and split the binary num into a list
        num = list('{0:036b}'.format(int(line[line.index("=")+2:])))
        # set the mask on the binary number list
        for i in range(len(mask)):
            if mask[i] != "X":
                num[i] = mask[i]
        # convert the binary num list back to a num and save it to memory
        mem[line[4:line.index("]")]] = int("".join(num), 2)

# Part Two