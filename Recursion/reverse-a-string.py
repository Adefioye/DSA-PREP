str1 = "kayaku"
str2 = "The Simple Engineer"


def reverseAString(input):
    if input == "":
        return ""

    return reverseAString(input[1:]) + input[0] 

print(reverseAString(str1))
print(reverseAString(str2))