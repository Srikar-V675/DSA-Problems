# Inversion Count
def merge(arr: list[int], low: int, mid: int, high: int) -> int:
    temp = []
    i = low
    j = mid + 1
    inversions = 0
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            inversions += ((mid-i) + 1)
            j += 1
    
    while i <= mid:
        temp.append(arr[i])
        i += 1
    
    while j <= high:
        temp.append(arr[j])
        j += 1
    
    for i in range(low, high+1):
        arr[i] = temp[i - low]
    
    return inversions

def mergeSort(arr: list[int], low: int, high: int):
    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr, low, mid, high)
