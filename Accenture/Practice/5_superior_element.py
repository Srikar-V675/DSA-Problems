# Superior Element in Array
def superior(arr: list[int]) -> int:
    count = 1
    greater = arr[len(arr) - 1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > greater:
            greater = arr[i]
            count += 1
    
    return count

arr: list[int] = [2, 8, 9, 7, 4, 2]
print(superior(arr))