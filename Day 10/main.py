# read the input file
inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()
for i in range(len(puzzleInput)):
    puzzleInput[i] = int(puzzleInput[i].rstrip("\n"))
puzzleInput.sort()
print(puzzleInput)

# # Part One
# counts = {1 : 1, 2 : 0, 3 : 1}
# for i in range(len(puzzleInput)-1):
#     counts[puzzleInput[i+1]-puzzleInput[i]] += 1

# print("Part One answer : ", str(counts[1]*counts[3]))
# # Part One



# Part Two
tree = {}
def createTree(num):
    arrangements = [x for x in puzzleInput if x <= num+3 and x > num]
    for e in arrangements:
        if e not in tree.keys():
            tree[e] = []
        tree[e].append()

for i in range(4):
    findArrangements()