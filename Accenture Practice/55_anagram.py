def are_anagrams(str1: str, str2: str) -> bool:
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Compare sorted characters
    return sorted(str1) == sorted(str2)

# Example usage
print(are_anagrams("Listen", "Silent"))  # Output: True
print(are_anagrams("Hello", "World"))    # Output: False
