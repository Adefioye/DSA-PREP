
# Brute force: time = 0(2 ^ n) and space = O(n)
# Using memoization: time = O(n) and space = O(n ^ 2)
# Note: I do believe, we kinda increase space for memoized version
# of the fib function. Since memo object is required which is
# additional space for every fib function call 

def fib(n, memo):
    
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return 1 
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)

    return memo[n]

print(fib(1, {}))   # 1
print(fib(2, {}))   # 1
print(fib(3, {}))   # 2
print(fib(7, {}))   # 13
print(fib(8, {}))   # 21
print(fib(50, {}))  # 12586269025