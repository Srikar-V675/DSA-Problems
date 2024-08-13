# Sort Even and Odd indexes of Array
from typing import List, Tuple

def evenOddSort(arr: List[int]) -> Tuple[List[int], List[int]]:
    return (sorted(
        [arr[i] for i in range(0, len(arr), 2)]), 
        sorted([arr[i] for i in range(1, len(arr), 2)])
        )

arr: List[int] = [3, 4, 1, 7, 9]
print(evenOddSort(arr))