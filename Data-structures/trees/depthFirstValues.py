class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b 
a.right = c 
b.left = d 
b.right = e 
c.right = f 

# Get values using DEPTH-FIRST SEARCH ALGORITHMS

# ITERATIVE VERSION

# def depthFirstValues(root):

#     if root == None:
#         return []

#     res = []
#     stack = [root]

#     while len(stack) > 0:
#         current = stack.pop()
#         res.append(current.val)

#         if current.right:
#             stack.append(current.right)
        
#         if current.left:
#             stack.append(current.left)  

    # return res 

# RECURSIVE VERSION OF DEPTH-FIRST SEARCH ALGORITHM

def depthFirstValues(root):

    if root == None:
        return []

    leftValues = depthFirstValues(root.left)
    rightValues = depthFirstValues(root.right)
    return [root.val] + leftValues + rightValues

print(depthFirstValues(a))

