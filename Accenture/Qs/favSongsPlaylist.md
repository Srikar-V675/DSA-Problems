---
dsa-patterns: 
- "[[Sliding-Window]]"
- "[[Strings]]"
difficulty: medium
companies: 
- Accenture
dg-publish: true
---
# Problem Statement

**Difficulty:** `Easy`

Thania has a favourite song and that is 'a'. Thania wants to find the maximum number of her favourite songs that can be present in the playlists of size k she can create from the input string(playlist) given.

Example:

```
Input:
songs = 'abaca'
size = k
Output:
2

Explanation:
From songs string we can generate 3 playlist of size k i.e 3, they are 'aba', 'bac', and 'aca'. Among these smaller playlists of size k, the maximum number of her favourite songs present in one of the size k playlists is 2.
```

# Approach

We can consider this as a `sliding window` problem. Where we compute the count of fav songs ('a') in the first window of size k. Then we can move the window by one place and increment count if new `right` is 'a' and decrement count if `left` that we removed from the window was 'a'.

# Code

**Time Complexity:** O(N)
**Space Complexity:** O(1)

```python
if 'a' not in songs:
    return 0
right = 0
count = 0
while right < k:
    if songs[right] == 'a':
        count += 1
    right += 1
maxCount = count
while right < len(songs):
    if songs[right] == 'a':
        count += 1
    left = right - k
    if somgs[left] == 'a':
        count -= 1
    maxCount = max(maxCount, count)
    right += 1
return maxCount
```