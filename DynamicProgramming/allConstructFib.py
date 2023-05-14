# time = O(n ^ m); space = O(n ^ m)

def allConstruct(target, wordBank):

    tab = [[]] * (len(target) + 1)
    tab[0] = [[]]

    for i in range(len(tab)):
        for word in wordBank:
            if target[i : i + len(word)] == word:
                newCombs = [[*item, word] for item in tab[i]]
                print(newCombs)
                print(tab[i + len(word)])
                tab[i + len(word)].extend(newCombs)

    return tab[len(target)]

print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))

## FIRST SOLUTION
# def allConstruct(target, wordBank):

#     tab = [None] * (len(target) + 1)
#     tab[0] = [[]]

#     for i in range(len(tab)):
#         if tab[i] is not None:
#             for word in wordBank:
#                 if target[i : i + len(word)] == word:
#                     if tab[i + len(word)] == None:
#                         tab[i + len(word)] = []
#                         for item in tab[i]:
#                             tab[i + len(word)].append([*item, word])
#                     else:
#                         for item in tab[i]:
#                             tab[i + len(word)].append([*item, word])

#     return tab[len(target)]