class node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

    def __repr__(self):
        return str({"value": self.value, "next": self.next})

class queue:
    def __init__(self):
        self.first = None 
        self.last = None 
        self.length = 0 
    
    def __str__(self):
        return str(self.__dict__) 

    def peek(self):
        return self.first
    
    def enqueue(self, value):
        new_node = node(value)

        if (self.first == None):
            self.first = new_node 
            self.last = self.first 
        else:
            self.last.next = new_node
            self.last = new_node
        
        self.length += 1 

        return self


    def dequeue(self):
        
        if (self.length == 0):
            return "No item in the queue" 

        if (self.first == self.last):
            self.last = None

        self.first = self.first.next 
        self.length -= 1 

        return self 

# Joy, Matt, Pavel, Samir 
my_stack = queue()

print(my_stack.peek())

print(my_stack.enqueue("Joy"))
print(my_stack.enqueue("Matt"))
print(my_stack.enqueue("Pavel"))
print(my_stack.enqueue("Samir"))

print(my_stack.dequeue())
print(my_stack.dequeue())
print(my_stack.dequeue())
print(my_stack.dequeue())
print(my_stack.dequeue())

