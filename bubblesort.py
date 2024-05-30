def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range (0, n - i - 1 ):
            if arr[j] > arr [ j+1 ]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [55, 23, 78, 22, 82, 11, 60]
bubblesort(arr)
print ("Sorted array is : ", arr)