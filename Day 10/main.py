# read the input file
inputFile = open("input.txt", "r")
puzzleInput = inputFile.readlines()
for i in range(len(puzzleInput)):
    puzzleInput[i] = int(puzzleInput[i].rstrip("\n"))
puzzleInput.sort()

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
    if len(arrangements) == 0:
        return
    if num not in tree.keys():
        tree[num] = []
    tree[num] = tree[num] + arrangements
    for e in arrangements:
        createTree(e)

def cleanTree():
    for e in tree.keys():
        tree[e] = list(set(tree[e]))

highestNum = max(puzzleInput)
arrangementCount = [0]
def countArrangements(num):
    if num == highestNum:
        arrangementCount[0] += 1
        return
    for e in tree[num]:
        countArrangements(e)

createTree(0)
cleanTree()
# print(tree)
countArrangements(0)
print(arrangementCount)

