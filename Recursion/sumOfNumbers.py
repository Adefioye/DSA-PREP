def sumOfNumbers(input):

    if input == 1:
        return input
    return input + sumOfNumbers(input - 1)


print(sumOfNumbers(10))
print(sumOfNumbers(12))
print(sumOfNumbers(5))