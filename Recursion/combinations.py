def combinations(elements):

    if len(elements) == 0:
        return [ [] ]
    
    firstEl = elements[0]
    rest = elements[1:]

    combsWithoutFirst = combinations(rest)
    combsWithFirst = []

    for item in combsWithoutFirst:
        combWithFirst = [*item, firstEl]
        combsWithFirst.append(combWithFirst)

    return [*combsWithFirst, *combsWithoutFirst]

print(combinations(["a", "b", "c"]))
print(combinations([]))