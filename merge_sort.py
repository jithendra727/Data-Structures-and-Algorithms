class MergeSort:
    # Method to sort an array using mergeSort
    def merge_sort(self, array, left, right):
        if left < right:
            # Find the middle point
            middle = left + (right - left) // 2

            # Recursively sort the first and second halves
            self.merge_sort(array, left, middle)
            self.merge_sort(array, middle + 1, right)

            # Merge the sorted halves
            self.merge(array, left, middle, right)

    # Method to merge two subarrays
    def merge(self, array, left, middle, right):
        # Sizes of two subarrays to be merged
        n1 = middle - left + 1
        n2 = right - middle

        # Temporary arrays
        L = [0] * n1
        R = [0] * n2

        # Copy data to temp arrays
        for i in range(0, n1):
            L[i] = array[left + i]
        for j in range(0, n2):
            R[j] = array[middle + 1 + j]

        # Merge the temp arrays

        # Initial indexes of first and second subarrays
        i, j, k = 0, 0, left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements of L[] if any
        while i < n1:
            array[k] = L[i]
            i += 1
            k += 1

        # Copy remaining elements of R[] if any
        while j < n2:
            array[k] = R[j]
            j += 1
            k += 1

    # Utility method to print the array
    @staticmethod
    def print_array(array):
        for i in array:
            print(i, end=" ")
        print()

# Main method to call mergeSort
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    
    print("Given Array")
    MergeSort.print_array(array)
    
    ms = MergeSort()
    ms.merge_sort(array, 0, len(array) - 1)
    
    print("\nSorted array")
    MergeSort.print_array(array)
