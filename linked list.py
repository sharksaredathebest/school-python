class nodes:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

    def getData(self):
        return self.data

    def getPointer(self):
        return self.pointer

linkedList = []
startPointer = 0
freePointer =0
endPointer = -1
# [0]    [1]     [2]
# apple orange   corn    apple -> corn -> orange
#  2      1       -1


linkedList.append(nodes("apple", startPointer))
linkedList.append(nodes("empty", -1))
linkedList.append(nodes("corn", -1))

def insert(data):
    global linkedList
    for i in range(len(linkedList)):
        if linkedList[i].getData() == "empty":
            newNode = nodes(data, -1)
            linkedList[i] = newNode
            break