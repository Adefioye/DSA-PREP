
# time = O(m*n); space = O(m)
def canSum(targetSum, nums):

    tab = [False] * (targetSum + 1)
    tab[0] = True 

    for i in range(len(tab)):
        for num in nums:

            if tab[i] == True:
                # Add i and num
                # if inbound, set the value to True 

                if i + num < len(tab):
                    tab[i + num] = True

    return tab[targetSum]


print(canSum(7, [2, 3]))            # True
print(canSum(7, [5, 3, 4, 7]))      # True
print(canSum(7, [2, 4]))            # False
print(canSum(8, [2, 3, 5]))         # True
print(canSum(300, [7, 14]))         # False