# DYNAMIC PROGRAMMING BY ALVIN

`DP can involve the following series of questions`
- Calculate teh 40th number of the fibonacci sequence.
- Count the number of different ways to move through a 6 by 9 grid
- Given a set of coins, how can we make 27 cents in the least number of coins
- Given a set of substrings, what are the possible ways to construct the string `potentpot`

`__MEMOIZATION RECIPE__`
1. Make it work
    - visualize the problem as a tree
    - implement the tree using recursion
    - test it (ensure correctness)
2. Make it efficient
    - add a memo object
    - add a base case to return memo values
    - store return values into memo 


- __CAN SUM__: `Can you do it? Yes/No (Decision problem)`
- __HOW SUM__: `How will you do it? (Combinatoric problem)`
- __BEST SUM__: `What is the *best* way to do it? (Optimization problem)`