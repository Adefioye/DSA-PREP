

# MY SOLUTION
def canConstruct(target, wordBank):

    tab = [False] * (len(target) + 1)
    tab[0] = True 

    for i in range(len(target) + 1):

        if tab[i] == True:
            for word in wordBank:

                if target[i:].startswith(word) and i + len(word) <= len(target):
                    tab[i + len(word)] = True

    return tab[len(target)]



# def canConstruct(target, wordBank):

#     tab = [False] * (len(target) + 1)
#     tab[0] = True

#     for i in range(len(tab)):

#         if tab[i] is True:

#             for word in wordBank:

#                 if target[i : i + len(word)] == word:
#                     tab[i + len(word)] = True 

#     return tab[len(target)]






print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))                   # TRUE
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))    # FALSE
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # TRUE
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee"
])) # FALSE