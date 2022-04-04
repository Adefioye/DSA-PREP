class node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

    def __repr__(self):
        return str({"value": self.value, "next": self.next})

class stack:
    def __init__(self):
        self.top = None 
        self.bottom = None 
        self.length = 0
    
    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.top 
        
    def push(self, value):
        new_node = node(value)

        if (self.top == None):
            self.top = new_node 
            self.bottom = self.top 
        else:
            former_top_node = self.top 
            self.top = new_node 
            new_node.next = former_top_node 
        
        self.length += 1 

        return self
        

    def pop(self):
        if (self.top == None):
            return "No item in the stack" 
        
        if (self.top == self.bottom):
            self.bottom = None 
            
        self.top = self.top.next
        self.length -= 1
        return self


my_stack = stack()
print(my_stack.peek())

print(my_stack.push("google"))
print(my_stack.push("udemy"))
print(my_stack.push("discord"))

print(my_stack.peek())

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
