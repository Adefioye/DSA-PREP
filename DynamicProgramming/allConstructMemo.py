"""
Write a function `allConstruct(target, wordBank)` that takes a target string
an array of strings.

The function should return a 2D array containing all of the ways that the `target`
can be constructed by concatenating elements of the `wordBank` array. Each element
of the 2D array should represent one combination that constructs the `target`

You may reuse elements of `wordBank` as many times as needed.
"""

# m = target string; n = number of words in array
# brute force: time = O(n^m * m) and space = O(m^2)
# Memoized version: time = O(m*n*m) and space = O(m^2)

# MY SOLUTION
def allConstruct(target, wordbank):

    if len(target) == 0:
        return [[]]
    
    allComb = []

    for word in wordbank:

        if target.startswith(word):
            rem = target[len(word):]
            remCombs = allConstruct(rem, wordbank)
            targetCombs = [[word, *comb] for comb in remCombs]
            allComb.extend(targetCombs)
            
    return allComb

print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))

# ALVINS SOLUTION
# def allConstruct(target, wordBank, memo):

#     if target in memo: 
#         return memo[target]
    
#     if len(target) == 0:
#         memo[target] = [[]]
#         return [[]]
    
#     res = []
#     for word in wordBank:

#         if target.startswith(word):
#             suffix = target[len(word):]
#             suffixWays = allConstruct(suffix, wordBank, memo)
#             targetWays = [[word, *way] for way in suffixWays] 
#             res.extend(targetWays)

#     memo[target] = res
#     return res

# print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"], {}))
# print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"], {}))
# print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
# print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"], {}))
