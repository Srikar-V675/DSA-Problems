def find_equilibrium(arr):
    total_sum = sum(arr)  # Total sum of the array
    left_sum = 0  # Initialize left sum
    
    for i in range(len(arr)):
        # Right sum is total sum minus the current element and left sum
        right_sum = total_sum - left_sum - arr[i]
        
        if left_sum == right_sum:
            return i + 1  # Return 1-based index of equilibrium element
        
        left_sum += arr[i]  # Update the left sum
    
    return "No Equilibrium element found"

# Input
n = int(input())
arr = list(map(int, input().strip()))

# Output
result = find_equilibrium(arr)
print(result)
