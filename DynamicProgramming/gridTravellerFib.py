
# time = O(m*n); space = O(m*n)
def gridTraveller(m, n):
    # 3 0, 1, 2, 3
    # m = 1(2); n = 1(2)
    tab = [[0] * (n + 1) for _ in range(m + 1)]

    tab[1][1] = 1 
    for r in range(m + 1):
        for c in range(n + 1):
            curr = tab[r][c]

            if r + 1 <= m:
                tab[r + 1][c] += curr 
            if c + 1 <= n:
                tab[r][c + 1] += curr 

    return tab[m][n]



print(gridTraveller(1, 1)) # 1
print(gridTraveller(2, 3)) # 3
print(gridTraveller(3, 2)) # 3
print(gridTraveller(3, 3)) # 6
print(gridTraveller(18, 18)) # 2333606220