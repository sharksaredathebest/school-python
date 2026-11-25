class nodes:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

    def getData(self):
        return self.data

    def getPointer(self):
        return self.pointer

headPointer = -1
tailPointer = -1
NumberItems = 0

linkedListbutitsaccaQueue = []

def Enqueue(data):
    global headPointer, tailPointer, NumberItems
    if NumberItems == 20:
        return False
    else:
        if NumberItems == 0:
            HeadPointer = 0

        tailPointer += 1
        newNode = nodes(data, tailPointer)
        linkedListbutitsaccaQueue.append(newNode)
        NumberItems += 1
        return True

def Dequeue():
    global headPointer, tailPointer, NumberItems
    if NumberItems == 0:
        return "-1"
    else:
        NumberItems -= 1
        headPointer += 1
        return linkedListbutitsaccaQueue[headPointer-1]

Enqueue(5)
Enqueue(6)
Enqueue(7)
Enqueue(8)

for i in range(4):
    print(linkedListbutitsaccaQueue[i].getData(), linkedListbutitsaccaQueue[i].getPointer())

Dequeue()

print("")

