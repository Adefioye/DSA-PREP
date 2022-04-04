class stack:
    def __init__(self):
        self.array = [] 

    def peek(self):
        if (len(self.array) == 0):
            return "No item in the stack"
        return self.array[len(self.array) - 1]

    def push(self, value):
        self.array.append(value)
        return self.array

    def pop(self):
        if (len(self.array) == 0):
            return "No item in the stack"

        self.array.pop()
        return self.array 


my_stack = stack()

print(my_stack.peek())

print(my_stack.push("google"))
print(my_stack.push("udemy"))
print(my_stack.push("discord"))

print(my_stack.pop())
print(my_stack.pop())
