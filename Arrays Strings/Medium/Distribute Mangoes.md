---
dsa-patterns: 
- '[[Combinations]]'
difficulty: medium
companies: 
- Accenture 
- Nagarro
dg-publish: true
---
# Problem Description

You are given m identical mangoes and n identical people. Your task is to find the number of ways to distribute the m mangoes among the n people such that each person can receive zero or more mangoes.

Example 1:
```
Input: m = 3, n = 2
Output: 4
Explanation:
The 4 possible distributions are:
1. [3, 0] - Person 1 gets 3 mangoes, Person 2 gets 0 mangoes.
2. [0, 3] - Person 1 gets 0 mangoes, Person 2 gets 3 mangoes.
3. [2, 1] - Person 1 gets 2 mangoes, Person 2 gets 1 mango.
4. [1, 2] - Person 1 gets 1 mango, Person 2 gets 2 mangoes.
```

Example 2:
```
Input: m = 5, n = 3
Output: 21
Explanation:
The 21 possible distributions include:
1. [5, 0, 0]
2. [0, 5, 0]
3. [0, 0, 5]
...
1.  [1, 2, 2]
```

Example 3:

```
Input: m = 0, n = 5
Output: 1
Explanation:
There is only one way to distribute 0 mangoes among 5 people: 
[0, 0, 0, 0, 0].
```

# Approach

This problem can be seen as a `Combinations` problem. Let's consider the mangoes as `*` and the dividers that divide the mangoes to n people as `|`.

Since we need to divide `m` mangoes among `n` people, we need to place `n-1` dividers to divide the mangoes among the people. This is a combination problem because eventhough the order of groups of mangoes might matter but not the order of dividers placed. Since we are performing selection by the dividers, this problem is using `Combinations`.

Example:

![Mangoes](DSA-Problems/Arrays%20Strings/Medium/image-3.png)

```
m = 5 mangoes
n = 3 people

We need to make `n-1` partitions to distribute to n people. Let's consider the mangoes as `*` and the dividers that divide the mangoes to n people as `|`. Let's take one example distribution:

[ ** | ** | * ]

Here we choose `n-1` dividers from `m+n-1` which is (mangoes + dividers). So it is selection of dividers among the objects(mangoes+dividers).
```



# Code

**Time Complexity:** O(N)
**Space Complexity:** O(1)

```python
def binomialCoefficient(n: int, k: int) -> int:
    if k > (n-k):
        k = n - k
    ans = 1
    for i in range(k):
        ans *= (n - i)
        ans //= (i + 1)
    return ans

def distributeMangoes(m: int, n: int):
    # ways -> (m + n -1)C(n-1)
    ways = binomialCoefficient((m+n-1), (n-1))
    return ways
```