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
        
        # Handle 2 special cases with other with sub cases under each special case

        # Special case 1: Value = root value
            
        if (value == self.root.value):
            # Root node with no child
            if (self.root.left == None and self.root.right == None):
                self.root = None 
                self.length -= 1

            
            elif (self.root.left or self.root.right):
                # Root node with 1 child to the left
                if (self.root.left and (self.root.right == None)):
                    self.root = self.root.left 
                    self.length -= 1

                # Root node with 1 child to the right
                elif ((self.root.left == None) and self.root.right):
                    self.root = self.root.right
                    self.length -= 1

                # Root node with 2 children 
                elif (self.root.left and self.root.right):
                    holding_pointer = self.root.right
                    
                    # Confirm 3 cases if holding pointer has no child, 1 child and 2 children
                    # No child
                    if (holding_pointer.left == None and holding_pointer.right == None):
                        holding_pointer.left = self.root.left 
                        self.root = self.root.right 
                        self.length -= 1
                    # 1 child 
                    elif (holding_pointer.left or holding_pointer.right):
                        # Child on the left
                        if (holding_pointer.left and (holding_pointer.right == None)):
                            min_node = holding_pointer.left 
                            min_node.left = self.root.left 
                            min_node.right = self.root.right 
                            holding_pointer.left = None 
                            self.root = min_node 
                            self.length -= 1
                        # child on the Right 
                        elif ((holding_pointer.left == None) and holding_pointer.right):
                            holding_pointer.left = self.root.left
                            self.root = self.root.right 
                            self.length -= 1 
                        # 2 children
                        elif (holding_pointer.left and holding_pointer.right):
                            parent_min_node = holding_pointer 
                            min_node = holding_pointer.left 
                            while (min_node.left != None):
                                parent_min_node = min_node 
                                min_node = min_node.left
                            
                            min_node.left = self.root.left 
                            min_node.right = self.root.right 
                            self.root = min_node
                            parent_min_node.left = None 
                            self.length -= 1

        # Special case 2: Handle Non-root node ( Access to parent node of the unwanted node very essential)
        else:
            
            result = self.lookup(value)

            if (type(result) == str):
                return result 

            else:
                parent_node = result["parent_node"]
                unwanted_node = result["current_node"]


                # Case 1: No child, hence find parent node and point to null
                if (unwanted_node.left == None and unwanted_node.right == None):
                    if (parent_node.left == unwanted_node):
                        parent_node.left = None 
                        self.length -= 1
                    elif parent_node.right == unwanted_node:
                        parent_node.right = None 
                        self.length -= 1 

                # Case 2: One child, hence point parent node to the child of the unwanted node
                elif (unwanted_node.left or unwanted_node.right):
                    if (unwanted_node.left and (unwanted_node.right == None)): # if unwanted node child is on left, point parent node to it
                        unwanted_node_child = unwanted_node.left 
                        if (parent_node.left == unwanted_node):
                            parent_node.left = unwanted_node_child
                            self.length -= 1
                    elif ((unwanted_node.left == None) and unwanted_node.right): # if unwanted node child is on right, point parent node to it
                        unwanted_node_child = unwanted_node.right 
                        if (parent_node.right == unwanted_node):
                            parent_node.right = unwanted_node_child
                            self.length -= 1


                # Case 3: 
                    elif (unwanted_node.left and unwanted_node.right):
                        holding_pointer = unwanted_node.right 

                    # if holding pointer(right sub tree) has no child, point right subtree to left child of unwanted node and point parent node to holding pointer
                        if ((holding_pointer.left == None) and (holding_pointer.right == None)):
                            holding_pointer.left = unwanted_node.left 
                            if parent_node.left == unwanted_node:
                                parent_node.left = holding_pointer 
                                self.length -= 1
                            elif parent_node.right == unwanted_node:
                                parent_node.right = holding_pointer 
                                self.length -= 1 
                        elif (holding_pointer.left or holding_pointer.right):
                            if (holding_pointer.left and (holding_pointer.right == None)):
                                parent_min_node = holding_pointer 
                                min_node = parent_min_node.left 

                                if parent_node.left == unwanted_node:
                                    parent_node.left = min_node 
                                elif parent_node.right == unwanted_node:
                                    parent_node.right = min_node 
                            
                                min_node.left = unwanted_node.left 
                                min_node.right = unwanted_node.right 
                                parent_min_node.left = None 
                                self.length -= 1 

                            elif ((holding_pointer.left == None) and holding_pointer.right):
                                if parent_node.left == unwanted_node:
                                    parent_node.left = holding_pointer 
                                    holding_pointer.left = unwanted_node.left 
                                    self.length -= 1 
                                elif parent_node.right == unwanted_node:
                                    parent_node.right = holding_pointer 
                                    holding_pointer.left = unwanted_node.left 
                                    self.length -= 1 

                            elif (holding_pointer.left and holding_pointer.right):
                                parent_min_node = holding_pointer 
                                min_node = parent_min_node 
                                while (min_node.left != None):
                                    parent_min_node = min_node 
                                    min_node = min_node.left 
                            
                                if parent_node.left == unwanted_node:
                                    parent_node.left = min_node 
                                elif parent_node.right == unwanted_node:
                                    parent_node.right = min_node

                                min_node.left = unwanted_node.left 
                                min_node.right = unwanted_node.right 
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
bst.remove(5)
print(bst)
bst.remove(3)
print(bst)
bst.remove(7)
print(bst) 
bst.remove(1)
print(bst)
bst.remove(0)
print(bst)
bst.remove(10)
print(bst)
bst.remove(65)
print(bst)




'''
        10
    5 
       6 
          12
        8
'''

