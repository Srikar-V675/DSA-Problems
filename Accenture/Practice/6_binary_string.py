# Binary String
def binaryStr(s: str) -> int:
    first = int(s[0])
    for i in range(1, len(s), 2):
        op = s[i]
        second = int(s[i+1])
        if op == 'A':
            first &= second
        elif op == 'B':
            first |= second
        else:
            first ^= second
    
    return first

s: str = '0C1A1B1C1C1B0A0'
print(binaryStr(s))