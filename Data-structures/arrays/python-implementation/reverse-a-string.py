my_string = "Hi! my name is Koko"

# print(len(my_string))

def reverse_a_string(string):
    reverse_string = []

    if (type(string) != str):
        return "Not a valid input, Try again"

    if (len(string) == 1):
        return string

    for i in range(len(string) - 1, -1, -1):
        reverse_string.append(string[i])
    return "".join(reverse_string) 

print(reverse_a_string(my_string))
print(reverse_a_string("a"))
print(reverse_a_string("abcd"))
print(reverse_a_string(["abcd"]))