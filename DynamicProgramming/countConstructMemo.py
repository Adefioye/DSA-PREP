"""
Write a function `countConstruct(target, wordBank)` that takes a target string
an array of strings.

The function should return the number of ways that the `target` can be constructed by
concatenating elements of the `wordBank` array.

You may reuse elements of `wordBank` as many times as needed.
"""

# m = target string; n = number of words in array
# brute force: time = O(n^m * m) and space = O(m^2)
# Memoized version: time = O(m*n*m) and space = O(m^2)
def countConstruct(target, wordBank, memo):
    
    if target in memo:
        return memo[target]
    
    if len(target) == 0:
        memo[target] = 1
        return 1 
    
    size = 0
    for word in wordBank:

        if target.find(word) == 0:
            suffix = target[len(word):]
            size += countConstruct(suffix, wordBank, memo)

    memo[target] = size
    return size

print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"], {}))                 # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))                 # 1
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))  # 0
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}))# 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
        "e",
        "ee",
        "eee",
        "eeee",
        "eeeee",
        "eeeeee"
        ], {})) # 0