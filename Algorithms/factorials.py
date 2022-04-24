# Find factorial
def factorial_iterative_approach(number):
    result = 1 
    if number == 0 or number == 1:
        return result 
    elif number == 2:
        return result * number
    else:
        for i in range(2, number + 1):
            result = result * i

    return result

def factorial_recursive_approach(number):
    result = 1
    if number == 0 or number == 1:
        return result
    
    return number * factorial_recursive_approach(number - 1)



print(factorial_iterative_approach(0))
print(factorial_iterative_approach(1))
print(factorial_iterative_approach(2))
print(factorial_iterative_approach(3))
print(factorial_iterative_approach(4))
print(factorial_iterative_approach(5))
print(factorial_iterative_approach(6))

print(factorial_recursive_approach(0))
print(factorial_recursive_approach(1))
print(factorial_recursive_approach(2))
print(factorial_recursive_approach(3))
print(factorial_recursive_approach(4))
print(factorial_recursive_approach(5))
print(factorial_recursive_approach(6))




