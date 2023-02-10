from collections import deque

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

# ITERATIVE VERSION
# def treeIncludes(root, target):
#     """
#     Check if target value exists in the tree data structure
#     """

#     if root == None:
#         return False 

#     queue = deque()
#     queue.append(root)

#     while len(queue) > 0:

#         current = queue.popleft()

        
#         if current.val == target:
#             return True 
        
#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)

        
#     return False

# RECURSIVE version of tree includes

def treeIncludes(root, target):

    if root == None:
        return False 
    
    if root.val == target:
        return True

    leftRes = treeIncludes(root.left, target)
    rightRes = treeIncludes(root.right, target)

    return leftRes or rightRes


print(treeIncludes(a, "e"))
print(treeIncludes(a, "c"))
print(treeIncludes(a, "k"))