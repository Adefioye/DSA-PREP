# Google question
array_1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]
array_2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
array_3 = [2, 3, 4, 5]

def first_recurring_character_1(array):
    map = {}

    # Check if item is not in map
    # If not initialize with 1
    # Otherwise add 1
    # Check if value = 2 then return item

    for item in array:
        if map.get(item):
            return item
        else:
            map[item] = item


    return "undefined"


print(first_recurring_character_1(array_1))
print(first_recurring_character_1(array_2))
print(first_recurring_character_1(array_3))