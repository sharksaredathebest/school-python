dalist = [3, 15, 16, 19, 25, 29, 32, 54, 72, 77]

searchitem = int(input("Enter the number you're looking for: "))
found = False
last = len(dalist)-1
first = 0

while found == False:
    middle = (last+first)//2
    if dalist[middle] == searchitem:
        found = True
        print("yay")
        print(middle)
    elif dalist[middle] < searchitem:
        found = False
        first = middle+1
    elif dalist[middle-1] > searchitem:
        found = False
        last = middle-1

if not found:
    print("no")