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

a.left = b 
a.right = c 
b.left = d 
b.right = e 
c.right = f 

# ITERATIVE VERSION of three sum

# def treeSum(root):
    
#     if root == None:
#         return 0 

#     res = 0
#     queue = deque()
#     queue.append(root)

#     while len(queue) > 0:
#         current = queue.popleft()

#         res += current.val 

#         if current.left:
#             queue.append(current.left)
        
#         if current.right:
#             queue.append(current.right)

#     return res


# RECURSIVE VERSION of three sum

def treeSum(root):

    if root == None:
        return 0 

    leftRes = treeSum(root.left)
    rightRes = treeSum(root.right)

    return root.val + leftRes + rightRes

#ANS = 25
print(treeSum(a))