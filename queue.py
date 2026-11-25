basePointer = 0
frontPointer = -1

maxSize = int(input("Enter the max size of the queue: "))

queue = [""]*maxSize

def enqueue(element):
    global frontPointer
    if frontPointer != maxSize-1:
        frontPointer += 1
        queue[frontPointer] = element
    else:
        print("Queue is full")

def dequeue():
    global basePointer
    if basePointer <= frontPointer:
        basePointer = basePointer + 1
    else:
        print("Queue is empty")

enqueue(input("Enter the element to be enqueued: "))
enqueue(input("Enter the element to be enqueued: "))
enqueue(input("Enter the element to be enqueued: "))
enqueue(input("Enter the element to be enqueued: "))

print(queue)

dequeue()

for i in range(basePointer, frontPointer):
    print(queue)