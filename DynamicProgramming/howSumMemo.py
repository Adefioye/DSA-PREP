"""
Write a function `howSum(targetSum, numbers)` that takes in a targetSum and
an array of numbers as arguments.

The function should return an array containing any combination of
elements that add up to exactly the targetSum. If there is no combination
that adds up to the targetSum, then return null.

If there are multiple combinations possible, you may return any
single one.
"""

# m = target number; n = number of elements in array
# Brute force: time = O(n^m * m), space = O(m)
# Memoized version: time = O(n* m^2), space = O(m^2)
def howSum(targetSum, nums, memo):

    if targetSum in memo:
        return memo[targetSum]
    
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None 
    
    for num in nums:
        rem = targetSum - num 
        remResult = howSum(rem, nums, memo)

        if remResult != None:
            memo[targetSum] = [*remResult, num]
            return memo[targetSum]

    memo[targetSum] = None    
    return None


print(howSum(7, [2, 3], {}))        # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7], {}))  # [4, 3]
print(howSum(7, [2, 4], {}))        # None 
print(howSum(8, [2, 3, 5], {}))     # [2, 2, 2, 2]
print(howSum(300, [7, 14], {}))     # None 