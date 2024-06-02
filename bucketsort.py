def bucketsort(array):
    if len(array) == 0:
        return array

    # Find the minimum and maximum values to normalize the array values
    min_value = min(array)
    max_value = max(array)

    # Create an array of empty buckets
    bucket_count = len(array)
    bucket = [[] for _ in range(bucket_count)]

    # Put array elements into different buckets
    for j in array:
        # Normalize the value to fall into the range [0, bucket_count - 1]
        index_b = (j - min_value) * (bucket_count - 1) // (max_value - min_value)
        bucket[index_b].append(j)

    # Sort each bucket and concatenate the results
    sorted_array = []
    for i in range(bucket_count):
        bucket[i] = sorted(bucket[i])
        sorted_array.extend(bucket[i])

    return sorted_array

array = [12, 84, 64, 65, 94, 46, 99]
print("Sorted array is:", bucketsort(array))
