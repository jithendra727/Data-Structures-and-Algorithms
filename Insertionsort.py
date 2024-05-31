def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1 ] = arr[j]
            j = j-1
            arr[j+1 ] = key

arr = [12,98,45,56,75,10,54,56,66]
insertionsort(arr)
print("Sorted array is : ", arr)