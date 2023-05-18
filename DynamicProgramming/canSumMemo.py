"""
CAN SUM PROBLEM 

Write a function `canSum(targetSum, nums)` that takes in a targetSum
and an array of numbers as arguments.

The function should return a boolean indicating whether or not it
is possible to generate the targetSum using the numbers from the array

You may use an element of the array as many times as needed 

You may assume that all input numbers are non-negative
"""

# ALVINS SOLUTION
# if m = target number and n = number of elements in number array
# Brute force: time = O(n ^ m) and space = O(m)
# Memoized version: time = O(n * m) and space = O(m)

# def canSum(targetSum, nums, memo):

#     if targetSum in memo:
#         return memo[targetSum]
    
#     if targetSum == 0:
#         return True 

#     if targetSum < 0:
#         return False 
    
#     for num in nums:
#         rem = targetSum - num
#         if canSum(rem, nums, memo):
#             memo[targetSum] = True
#             return True

#     memo[targetSum] = False 
#     return False

# print(canSum(7, [2, 3], {}))            # True
# print(canSum(7, [5, 3, 4, 7], {}))      # True
# print(canSum(7, [2, 4], {}))            # False
# print(canSum(8, [2, 3, 5], {}))         # True
# print(canSum(300, [7, 14], {}))         # False


# MY SOLUTION
def canSum(targetSum, nums):

    def dfs(i, pathSum):

        if i >= len(nums) and targetSum == pathSum:
            return True 
        
        if i >= len(nums) and targetSum != pathSum:
            return False 

        if pathSum > targetSum:
            return False 

        if targetSum == pathSum:
            return True 

        # Decision to add nums[i] 
        addNum = dfs(i, pathSum + nums[i])

        # Decision not to add nums[i] 
        dontAddNum = dfs(i + 1, pathSum)

        return addNum or dontAddNum


    return dfs(0, 0)

print(canSum(7, [2, 3]))            # True
print(canSum(7, [5, 3, 4, 7]))      # True
print(canSum(7, [2, 4]))            # False
print(canSum(8, [2, 3, 5]))         # True
print(canSum(300, [7, 14]))         # False
