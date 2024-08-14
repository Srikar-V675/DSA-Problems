# Decimal to N-Base
def dec2Nbase(n: int, num: int) -> str:
    remainder = []
    qoutient = num // n
    rem = num % n
    if rem > 9:
        alpha = rem - 9
        alpha = alpha + 64 # 64 -> ASCII => 'A'
        remainder.append(chr(alpha))
    else:
        remainder.append(str(rem))
    while qoutient != 0:
        rem = qoutient % n
        qoutient //= n
        if rem > 9:
            alpha = rem - 9
            alpha = alpha + 64 # 64 -> ASCII => 'A'
            remainder.append(chr(alpha))
        else:
            remainder.append(str(rem))
    
    return ''.join(remainder[::-1])

n = 12
num = 718
print(dec2Nbase(n, num))