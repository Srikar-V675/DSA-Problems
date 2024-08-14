# Convert a Given String to Palindrome
def convertPalin(s: str) -> str:
    if s == s[::-1]:
        return s
    add = ''
    for ch in s:
        add += ch
        palin = s + add[::-1]
        if palin == palin[::-1]:
            return palin
    

s: str = 'abcdc'
print(convertPalin(s))