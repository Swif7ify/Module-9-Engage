def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

values = [23, 10, 5, 1, 18, 31, 16]

print("Insertion Sort:", insertion_sort(values.copy()))
