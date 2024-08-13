# Number of Carries
def numCarry(num1: int, num2: int) -> int:
    carries = 0
    carry = 0
    while num1 != 0 and num2 != 0:
        sum = (num1%10) + (num2%10) + carry
        num1 //= 10
        num2 //= 10
        if sum > 9:
            carries += 1
            carry = 1
        else:
            carry = 0
    return carries

num1 = 451
num2 = 349
print(numCarry(num1, num2))