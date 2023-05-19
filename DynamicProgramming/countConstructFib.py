
# time = O(m*n*m) and space = O(m)

# MY SOLUTION
def countConstruct(target, wordBank):

    tab = [0] * (len(target) + 1)
    tab[0] = 1 

    for i in range(len(target) + 1):

        if tab[i] != 0:

            for word in wordBank:

                if target[i:].startswith(word) and i + len(word) <= len(target):
                    tab[i + len(word)] += tab[i]

    return tab[len(target)]

# ALVINS SOLUTION
# def countConstruct(target, wordBank):
#     tab = [0] * (len(target) + 1)
#     tab[0] = 1

#     for i in range(len(tab)):
#         for word in wordBank:

#             if target[i : i + len(word)] == word:
#                 tab[i + len(word)] += tab[i]

#     return tab[len(target)]

print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))                 # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))                 # 1
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))# 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
        "e",
        "ee",
        "eee",
        "eeee",
        "eeeee",
        "eeeeee"
        ])) # 0