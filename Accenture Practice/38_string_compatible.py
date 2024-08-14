def are_compatible(str1: str, str2: str) -> str:
    max_diff = ord(str2[0]) - ord(str1[0])
    if max_diff > 0:
        for i in range(1, len(str1)):
            diff = ord(str2[i]) - ord(str1[i])
            if diff > max_diff:
                return "NO"
        return "YES"
    else:
        return "NO"

# Example usage:
str1 = input()
str2 = input()
print(are_compatible(str1, str2))
