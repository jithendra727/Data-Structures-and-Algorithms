def selection(a):
    for i in range(len(a)):
        small = i 
        for j in range(i+1, len(a)):
            if a[samll] > a [j]:
                samll = j
            a[i], a[small] = a[small], a[i]

def printArr(a):
    for i in range(len(a)):
        print(a[i], end = " ")

a = [68, 45, 12, 32, 5, 4]
print("Before sorting array elements are - ")  
printArr(a)  
selection(a)  
print("\nAfter sorting array elements are - ")  
selection(a)  
printArr(a)