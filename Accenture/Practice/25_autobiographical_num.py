# Find unique digits in Autobiographical Number
def autobioNum(num: str) -> int:
    freq = {}
    for n in num:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    for i in range(len(num)):
        if str(i) in freq:
            if freq[str(i)] != int(num[i]):
                return 0
        else:
            if num[i] != '0':
                return 0
    return len(freq)


num: str = '1210'
print(autobioNum(num))