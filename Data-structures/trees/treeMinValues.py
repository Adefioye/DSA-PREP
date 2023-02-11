from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

p = Node(5)
q = Node(11)
w = Node(3)
x = Node(4)
y = Node(15)
z = Node(12)

a.left = b 
a.right = c 
b.left = d 
b.right = e 
c.right = f 

p.left = q
p.right = w
q.left = x
q.right = y
w.right = z

# ITERATIVE APPROACH
# def treeMinValues(root):

#     if root == None: 
#         return float("inf")

#     minVal = float("inf")
#     queue = deque()
#     queue.append(root)

#     while len(queue) > 0:
#         current = queue.popleft()

#         minVal = min(minVal, current.val)

#         if current.left:
#             queue.append(current.left)
#         if current.right:
#             queue.append(current.right)

#     return minVal

# RECURSIVE APPROACH
def treeMinValues(root):
    if root == None: 
        return float("inf")

    return min(root.val, treeMinValues(root.left), treeMinValues(root.right))

print(treeMinValues(a))
print(treeMinValues(p))