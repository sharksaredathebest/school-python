import random

# initialising

topOfStack = -1
maxvalues = 30
nullPointer = 0
fullList = False
max = 0
min = 99999999

stack = [0 for i in range(maxvalues)]

# functions

def push(item):
    global topOfStack
    global fullList

    if topOfStack < maxvalues:
        stack[topOfStack] = item
        topOfStack += 1
        return True
    else:
        fullList = True
        return False

def pop():
    global topOfStack

    if topOfStack == nullPointer:
        print("-999")
    else:
        topOfStack -= 1
        print(stack[topOfStack])

def FindValues():
    global max, min

    while topOfStack > 0:
        if stack[topOfStack - 1] < min:
            min = stack[topOfStack - 1]
        if stack[topOfStack - 1] > max:
            max = stack[topOfStack - 1]

        pop()

    print("min:", min)
    print("max:", max)


#executing the code

while not fullList:
    randNum = random.randint(0, 1001)
    push(randNum)

print(stack)

FindValues()