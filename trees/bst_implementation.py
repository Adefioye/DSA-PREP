from anyio import current_time
from sqlalchemy import null


class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str({"value": self.value, "left": self.left, "right": self.right})

class binary_search_tree:
    def __init__(self):
        self.root = None 
        self.length = 0 

    def __str__(self):
        return str(self.__dict__)

    def insert(self, value):
        new_node = node(value)
        # Check if root is None and assign root to new Node
        if (self.root == None):
            self.root = new_node
            self.length += 1
            return self
        else:
            current_node = self.root
            while True:
                if (value < current_node.value): # if value less than current value go left
                    if (current_node.left == None): # if no value on left of current node, assign current node to new node and point parent node left pointer to current node
                        current_node.left = new_node
                        self.length += 1
                        return self
                    else:
                        current_node = current_node.left
                else:
                    if (current_node.right == None):
                        current_node.right = new_node
                        self.length += 1
                        return self
                    else: 
                        current_node = current_node.right

    def lookup(self, value):
        # check if root is None and return No element in tree
        # if root is not None, check if value is in root if not
        # check if value is < than root value, if yes go left
        # if value is > root value, if yes go right 
        # otherwise value
        if (self.root == None):
            return "No element in the tree"
        else:
            current_node = self.root
            parent_node = self.root
            while True:
                if (value < current_node.value):
                    if (current_node.left == None):
                        return f"{value} not Found"
                    parent_node = current_node
                    current_node = current_node.left 
                elif (value > current_node.value):
                    if (current_node.right == None):
                        return f"{value} not Found"
                    parent_node = current_node
                    current_node = current_node.right 
                else:
                    return {"parent_node": parent_node, "current_node": current_node}

    def remove(self, value):
        # 3 cases to be dealt with
        # Case 1: Node with no child, remove by point parent node to null
        # Case 2: Node with 1 child, remove by pointing parent node right/ left(anyone which exist) to child of unwanted node
        # Case 3: Node with 2 children, find minimum in right subtree, point it to parent node and delete it in former right subtree

        # if (self.root == None):
        #      return "No element in the tree"
        # else:

        result = self.lookup(value)

        if (type(result) == str):
            return result 

        else:
            parent_node = result["parent_node"]
            unwanted_node = result["current_node"]

            # Case 1: No child, hence find parent node and point to null
            if (unwanted_node.left == None and unwanted_node.right == None):
                if parent_node.left == unwanted_node:
                    parent_node.left = None 
                    self.length -= 1
                elif parent_node.right == unwanted_node:
                    parent_node.right = None 
                    self.length -= 1 

            # Case 2: One child, hence point parent node to the child of the unwanted node
            elif (unwanted_node.left or unwanted_node.right):
                if unwanted_node.left:
                    unwanted_node_child = unwanted_node.left 
                else:
                    unwanted_node_child = unwanted_node.right 

                if parent_node.left == unwanted_node:
                    parent_node.left = unwanted_node_child
                    self.length -= 1
                elif parent_node.right == unwanted_node:
                    parent_node.right = unwanted_node_child
                    self.length -= 1 

            # Case 3: Two children, find minimum node of right subtree, copy and point parent node to it and delete it from original position in right subtree
            elif (unwanted_node.left and unwanted_node.right):
                right_child_sub_tree = unwanted_node.right 

                # Find minimum node on right subtree and its parent
                min_node = right_child_sub_tree 
                parent_min_node = right_child_sub_tree
                while (min_node.left != None):
                    parent_node = min_node 
                    min_node = min_node.left 
                
                if (parent_node.left == unwanted_node):
                    parent_node.left = min_node 
                    min_node.right = right_child_sub_tree 
                    parent_min_node.left = None 
                    self.length -=1

                elif (parent_node.right == unwanted_node):
                    parent_node.right = min_node
                    min_node.right = right_child_sub_tree 
                    parent_min_node.left = None 
                    self.length -= 1


        return self.root

    def print_tree(self):
        if (self.root != None):
            self.printt(self.root)

    def printt(self, current_node):
        if (current_node != None):
            self.printt(current_node.left)
            print(str(current_node.value))
            self.printt(current_node.right)


bst = binary_search_tree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(13)
bst.insert(65)
bst.insert(0)
bst.insert(10)

bst.remove(13)
print(bst)


'''
        10
    5 
       6 
          12
        8
'''

