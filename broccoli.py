DataArray=[0, 3, 4, 56, 67, 44, 43, 32, 31, 345, 45, 6, 54, 1]

def InsertionSort(array):
    for i in range(len(array)):
        item =array[i]
        j = i-1
        while j>-1 and item<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1] = item

def OutputArray(array):
    output = ""
    for i in range(len(array)):
        output = output + " " + str(array[i])
    print(output)

OutputArray(DataArray)
InsertionSort(DataArray)
OutputArray(DataArray)

def searchArray(array,item):
    found = False
    for i in range(len(array)):
        if item == array[i]:
            print("Found at index "+str(i))
            found=True
    if found==False:
        print("Not found")

searchArray(DataArray,0)
searchArray(DataArray,345)
searchArray(DataArray,67)
searchArray(DataArray,2)
