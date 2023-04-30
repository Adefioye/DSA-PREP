"""
GRID TRAVELLER PROBLEM

Say that you are a traveller on a 2D grid. You give in the TOP-LEFT corner
and your goal is to travel to the BOTTOM-RIGHT corner. You may only move down
or right.

In how many ways can one travel to the goal on a grid with dimensions m*n?

Write a function `gridTraveller(m, n)` that calculates this.
"""

# Brute force: time = 0(2 ^ (m+n)) and space = O(m+n)
# Using memoization: time = O(m * n) and space = O(n)
def gridTraveller(m, n, memo):
    key = f"{m},{n}"

    if key in memo:
        return memo[key]
    
    if m == 1 and n == 1:
        return 1 
    
    if m == 0 or n == 0:
        return 0
    
    memo[key] = gridTraveller(m - 1, n, memo) + gridTraveller(m, n - 1, memo)

    return memo[key]



print(gridTraveller(1, 1, {})) # 1
print(gridTraveller(2, 3, {})) # 3
print(gridTraveller(3, 2, {})) # 3
print(gridTraveller(3, 3, {})) # 6
print(gridTraveller(18, 18, {})) # 2333606220