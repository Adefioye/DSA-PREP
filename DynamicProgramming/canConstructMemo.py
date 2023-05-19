"""
Write a function `canConstruct(target, wordBank)` that takes a target string
an array of strings.

The function should return a boolean indicating whether or not the `target` can
be constructed by concatenating elements of a `wordBank` array.

You may reuse elements of `wordBank` as many times as needed.
"""

# m = target string; n = number of words in array
# brute force: time = O(n^m * m) and space = O(m^2)
# Memoized version: time = O(m*n*m) and space = O(m^2)

# MY SOLUTION 
def canConstruct(target, wordBank, memo):

    if target in memo:
        return memo[target]
    
    if len(target) == 0:
        return True 
    
    for word in wordBank:

        if target.startswith(word):
            rem = target[len(word):]
            if canConstruct(rem, wordBank, memo):
                memo[target] = True
                return True
            
    memo[target] = False
    return False

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))                   # TRUE
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))    # FALSE
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}))  # TRUE
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
], {})) # FALSE

# ALVINS SOLUTION
# def canConstruct(target, wordBank, memo):

#     if target in memo:
#         return memo[target]
    
#     if len(target) == 0:
#         return True 
    
#     for word in wordBank:

#         if target.find(word) == 0:
#             suffix = target[len(word):]
#             if canConstruct(suffix, wordBank, memo):
#                 memo[target] = True
#                 return True
            
#     memo[target]  = False
#     return False


# print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))                   # TRUE
# print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))    # FALSE
# print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}))  # TRUE
# print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
#     "e",
#     "ee",
#     "eee",
#     "eeee",
#     "eeeee",
#     "eeeeee"
# ], {})) # FALSE