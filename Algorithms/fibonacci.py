# Given a number N return its value in the fibonacci sequence 

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 

def fibonacci_iterative_approach(n):
    temp_1 = 0
    temp_2 = 1
    if n == 0:
        return temp_1
    elif n == 1:
        return temp_2
    
    temp_3 = 0
    for i in range(2, n+1):
        temp_3 = temp_1 + temp_2
        temp_1 = temp_2 
        temp_2 = temp_3

    return temp_3

def fibonacci_recursive_approach(n):
    temp_1 = 0 
    temp_2 = 1
    if n == 0:
        return temp_1 
    elif n == 1:
        return temp_2
    
    return fibonacci_recursive_approach(n - 2) + fibonacci_recursive_approach(n - 1)




# print(fibonacci_iterative_approach(0))
# print(fibonacci_iterative_approach(1))
# print(fibonacci_iterative_approach(2))
# print(fibonacci_iterative_approach(3))
# print(fibonacci_iterative_approach(4))
# print(fibonacci_iterative_approach(5))
# print(fibonacci_iterative_approach(6))
# print(fibonacci_iterative_approach(7))
# print(fibonacci_iterative_approach(8))
# print(fibonacci_iterative_approach(9))
# print(fibonacci_iterative_approach(10))
# print(fibonacci_iterative_approach(11))
# print(fibonacci_iterative_approach(12))
# print(fibonacci_iterative_approach(13))
# print(fibonacci_iterative_approach(14))

print(fibonacci_recursive_approach(0))
print(fibonacci_recursive_approach(1))
print(fibonacci_recursive_approach(2))
print(fibonacci_recursive_approach(3))
print(fibonacci_recursive_approach(4))
print(fibonacci_recursive_approach(5))
print(fibonacci_recursive_approach(6))
print(fibonacci_recursive_approach(7))
print(fibonacci_recursive_approach(8))
print(fibonacci_recursive_approach(9))
print(fibonacci_recursive_approach(10))
print(fibonacci_recursive_approach(11))
print(fibonacci_recursive_approach(12))
print(fibonacci_recursive_approach(13))
print(fibonacci_recursive_approach(14))
