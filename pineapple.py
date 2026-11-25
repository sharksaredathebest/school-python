numbers=[47, 6, 54, 17, 93, 28]
def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]

    print(numbers)

# sort(numbers)

def insertionsort(array):
    for i in range(len(array)):
        item =array[i]
        j = i-1
        while j>-1 and item<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1] = item
        print(array)

insertionsort(numbers)
