
# time = O(m*n); space = O(m*n)

def gridTraveller(m, n):

    tab = [[0] * (n + 1) for _ in range(m + 1)]
    tab[1][1] = 1 

    for r in range(m + 1):
        for c in range(n + 1):

            if (r, c) != (1, 1):
                # top is r - 1
                if 0 <= r - 1 <= m:
                    tab[r][c] += tab[r - 1][c]

                # left is c - 1
                if 0 <= c - 1 <= n:
                    tab[r][c] += tab[r][c - 1]

    return tab[m][n]
# ALVINS SOLUTION
# def gridTraveller(m, n):
#     # 3 0, 1, 2, 3
#     # m = 1(2); n = 1(2)
#     tab = [[0] * (n + 1) for _ in range(m + 1)]

#     tab[1][1] = 1 
#     for r in range(m + 1):
#         for c in range(n + 1):
#             curr = tab[r][c]

#             if r + 1 <= m:
#                 tab[r + 1][c] += curr 
#             if c + 1 <= n:
#                 tab[r][c + 1] += curr 

#     return tab[m][n]



print(gridTraveller(1, 1)) # 1
print(gridTraveller(2, 3)) # 3
print(gridTraveller(3, 2)) # 3
print(gridTraveller(3, 3)) # 6
print(gridTraveller(18, 18)) # 2333606220