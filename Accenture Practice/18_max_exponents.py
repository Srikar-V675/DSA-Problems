# Max Exponents of 2
def maxExponents(n1: int, n2: int) -> int:
    maxNum = 0
    maxExpo = 0
    for num in range(n1, n2+1):
        expo = countExponents(num)
        if expo > maxExpo:
            maxExpo = expo
            maxNum = num
    return maxNum


def countExponents(num: int) -> int:
    count = 0
    while num % 2 == 0 and num != 0:
        count += 1
        num //= 2
    return count


n1 = 7
n2 = 12
print(maxExponents(n1, n2))