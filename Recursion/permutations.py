def permutations(elements):

    if len(elements) == 0:
        return [ [] ]
    
    firstEl = elements[0]
    rest = elements[1:]

    permsWithoutFirst = permutations(rest)
    allPermutations = []

    for _, item in enumerate(permsWithoutFirst):
        
        for i in range(len(item) + 1):
            permWithFirst = [*item[:i], firstEl, *item[i:]]
            allPermutations.append(permWithFirst)

    return allPermutations

print(permutations(["a", "b", "c"]))