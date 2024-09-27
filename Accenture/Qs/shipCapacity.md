---
dsa-patterns: math
difficulty: easy
companies: Accenture
dg-publish: true
---

# Problem Statement

There are two inputs C and N given, where C represents the capacity of a ship and N represents the number of people to transport. Determine how many rounds does the ship with capacity C have to take to transport N people from point A to point B.

Examples:

```
Input:
C = 50
N = 200
Output:
4 rounds

Explanation: Since it can take 50 people from point A to point B at a time, it would need to 4 rounds to transport all 200.
```

# Code

```python
rounds = N / C
if rounds > int(rounds):
    return int(rounds) + 1
else:
    return int(rounds)
```