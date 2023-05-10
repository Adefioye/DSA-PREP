


def howSum(targetSum, nums):

    tab = [None] * (targetSum + 1)
    tab[0] = []

    for i in range(targetSum + 1):

        for num in nums:

            if tab[i] is not None and (i + num) < len(tab):

                    tab[i + num] = [*tab[i], num]

    return tab[targetSum]

    return 
print(howSum(7, [2, 3]))        # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7]))  # [4, 3]
print(howSum(7, [2, 4]))        # None 
print(howSum(8, [2, 3, 5]))     # [2, 2, 2, 2]
print(howSum(300, [7, 14]))     # None 

print(None == [])