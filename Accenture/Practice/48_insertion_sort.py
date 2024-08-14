def insertion_sort(arr):
    # Implementing insertion sort algorithm
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Input section
N = int(input())  # Number of elements in the array
arr = list(map(int, input().strip()))  # Array elements as integers

# Sort the array using insertion sort
insertion_sort(arr)

# Output the sorted array elements
print(''.join(map(str, arr)))
