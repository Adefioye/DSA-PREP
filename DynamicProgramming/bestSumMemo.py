"""
Write a function `bestSum(targetSum, numbers)` that takes in a targetSum and
an array of numbers as arguments.

The function should return an array containing the shortest combination of 
numbers that add up exactly to the targetSum.

If there is a tie for the shortest combination, you may return any one 
of the shortest.
"""

# m = target no n = number of elements in array
# brute force: time = O(n^m * m) and space = O(m^2)
# Memoized version: time = O(m*n*m) and space = O(m^2)
def bestSum(targetSum, nums, memo):

    if targetSum in memo:
        return memo[targetSum]
    
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None 
    
    shortestComb = None 

    for num in nums:
        rem = targetSum - num 
        remComb = bestSum(rem, nums, memo)

        if remComb is not None:
            comb = [*remComb, num]

            if shortestComb is None or len(comb) < len(shortestComb):
                shortestComb = comb

    memo[targetSum] = shortestComb
    return shortestComb

print(bestSum(7, [5, 3, 4, 7], {}))         # [7]
print(bestSum(8, [2, 3, 5], {}))            # [3, 5]
print(bestSum(8, [1, 4, 5], {}))            # [4, 4]
print(bestSum(100, [1, 2, 5, 25], {}))      # [25, 25, 25, 25]
