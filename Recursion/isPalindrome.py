str1 = "racecar"    # True
str2 = "kayak"      # True
str3 = "box"        # False
def isPalindrome(input):
    # Define base case
    # If empty string / string has a length of 1, return true
    if len(input) == 0 or len(input) == 1:
        return True

    # Check if first and last element of problem space are same and reduce problem space
    if input[0] == input[len(input) - 1]:
        return isPalindrome(input[1: len(input) - 1])

    return False

print(isPalindrome(str1))
print(isPalindrome(str2))
print(isPalindrome(str3))