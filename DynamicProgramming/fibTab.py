
# time = O(n) and space = O(n)
def fib(n):

    if n <= 2:
        return 1
    
    tab = [0] * (n + 1)
    tab[1] = 1 

    for i in range(n):
        if i + 1 <= n:
            tab[i + 1] += tab[i]
        if i + 2 <= n:
            tab[i + 2] += tab[i]

    # print(tab)
    return tab[n]

print(fib(1))   # 1
print(fib(2))   # 1
print(fib(3))   # 2
print(fib(7))   # 13
print(fib(8))   # 21
print(fib(50))  # 12586269025