Queue = [-1 for i in range(20)]

# Initialising pointers
HeadPointer = -1
TailPointer = -1
NumberItems = 0

def Enqueue(num):
    global HeadPointer, TailPointer, NumberItems
    if NumberItems == 20:
        return False
    else:
        if NumberItems == 0:
            HeadPointer = 0

        TailPointer += 1
        Queue[TailPointer] = num
        NumberItems += 1
        return True

def Dequeue():
    global HeadPointer, TailPointer, NumberItems
    if NumberItems == 0:
        return "-1"
    else:
        NumberItems -= 1
        HeadPointer += 1
        return Queue[HeadPointer-1]

for i in range(1, 26):
    if Enqueue(i) == False:
        print(i, ", Unsuccessful")
    else:
        print(i, ", Successful")

print(Queue)

print(Dequeue())
print(Dequeue())
