# time = O(m*n*m); space = O(m * m)
def bestSum(targetSum, nums):

    tab = [None] * (targetSum + 1)
    tab[0] = []

    for i in range(len(tab)):
        for num in nums:

            if tab[i] is not None:

                if i + num < len(tab):
                    tempArray = [*tab[i], num] 

                    if tab[i + num] is None:
                        tab[i + num] = tempArray 
                    else:
                        if len(tempArray) < len(tab[i + num]):
                            tab[i + num] = tempArray 

    return tab[targetSum]

print(bestSum(7, [2, 3]))        # [2, 3, 2]
print(bestSum(7, [5, 3, 4, 7]))  # [7]
print(bestSum(7, [2, 4]))        # None 
print(bestSum(8, [2, 3, 5]))     # [3, 5]
print(bestSum(300, [7, 14]))     # None 
print(bestSum(8, [1, 4, 5]))    # [4, 4]
print(bestSum(100, [1, 2, 5, 25]))    # [25, 25, 25, 25]