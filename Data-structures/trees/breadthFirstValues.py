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

def breadthFirstValues(root):

    if root == None:
        return []

    res = []
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        current = queue.popleft()
        res.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return res

print(breadthFirstValues(a))