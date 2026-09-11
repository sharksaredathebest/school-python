DataStored = []
NumberItems = 0

def initialise():
    global NumberItems
    NumberItems = int(input("Input the quantity of numbers:  "))
    while NumberItems < 1 or  NumberItems > 20:
        NumberItems = int(input("Out of range please try again:  "))

    for i in range(NumberItems):
        num = int(input("Enter your value:"))
        DataStored.append(num)

initialise()
print(DataStored)

def bubble_sort():
    global DataStored
    for i in range(NumberItems):
        for b in range(NumberItems-1):
            if DataStored[b] > DataStored[b+1]:
                temp = DataStored[b]
                DataStored[b] = DataStored[b+1]
                DataStored[b+1] = temp


bubble_sort()
print(DataStored)