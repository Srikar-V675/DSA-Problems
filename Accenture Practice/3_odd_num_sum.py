# Sum of Odd Numbers in Array
def oddSum(arr: list[int]) -> int:
    sum = 0
    for num in arr:
        if num % 2 == 1:
            sum += num
    return sum

arr: list[int] = [1, 4, 6, 7, 10, 12, 11, 5]
print("Output: ", oddSum(arr))