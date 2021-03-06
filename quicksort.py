
def partition(arr,low,high):
    i=low-1

    pivot = arr[high]

    for j in range(low,high):
        if arr[high] >= arr[j]:
            i=i+1
            arr[i],arr[j] =arr[j],arr[i]
            arr[i+1],arr[high] = arr[high],arr[i+1]

    return i+1
            

def quicksort(arr,low,high):
    if high > low:
        p1 = partition(arr,low,high)

        quicksort(arr,low,high-1)
        quicksort(arr,low+1,high)

def input1():
    arr=[0, 1, 2, 8, 7, 6, 9]
    size = len(arr)-1

    quicksort(arr,0,size-1)

    print(arr)

input1()