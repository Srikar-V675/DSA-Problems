# Edwards Bday & Regions on a plane are same problems. 
def edwardBday(cuts: int) -> int:
    mod = 1000000007
    pieces = (cuts * (cuts + 1) // 2) + 1
    return pieces % mod

print("Output: ", edwardBday(5))