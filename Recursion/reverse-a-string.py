str1 = "kayaku"
str2 = "The Simple Engineer"


def reverseAString(input):
    # Define base case
    if input == "":
        return ""

    # Reduce the problem space
    # Perform a simple job needed to move closer to the solution
    return reverseAString(input[1:]) + input[0] 

print(reverseAString(str1))
print(reverseAString(str2))