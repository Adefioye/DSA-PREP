class node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.__dict__)


class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = self.head 
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def print_list(self):
        values_array = []
        current_node = self.head
        while (current_node):
            values_array.append(current_node.value)
            current_node = current_node.next

        print(self.length)
        return values_array

    def append(self, value):
        new_node = node(value)
        if (self.head == None):
            self.head = new_node 
            self.tail = self.head 
            self.length += 1 
        else:
            new_node.previous = self.tail 
            self.tail.next = new_node 
            self.tail = new_node 
            self.length += 1

    def prepend(self, value):
        new_node = node(value)
        if (self.head == None):
            self.head = new_node 
            self.tail = self.head 
            self.length += 1 
        else:
            new_node.next = self.head 
            self.head.previous = new_node 
            self.head = new_node 
            self.length += 1

    def insert(self, index, value):
        if (index > self.length - 1):
            self.append(value)
        elif (index == 0):
            self.prepend(value)
        else:
            new_node = node(value)
            leader_node = self.traverse_to_index(index - 1)
            follower_node = leader_node.next 
            leader_node.next = new_node 
            new_node.previous = leader_node 
            new_node.next = follower_node 
            follower_node.previous = new_node 
            self.length += 1
    
    def remove(self, index):
        if (self.head == None):
            return "No item in the list" 

        elif (index > self.length - 1):
            return "Index out of range" 

        elif (index == 0):
            unwanted_node = self.head 
            self.head = unwanted_node.next 
            self.head.previous = None
            self.length -= 1

        elif (index == self.length - 1):
            unwanted_node = self.tail 
            self.tail = unwanted_node.previous 
            self.tail.next = None 
            self.length -= 1
        else:
            leader_node = self.traverse_to_index(index -1)
            unwanted_node = leader_node.next 
            follower_node = unwanted_node.next 
            leader_node.next = follower_node 
            follower_node.previous = leader_node 
            self.length -= 1      

    def traverse_to_index(self, index):
        current_node = self.head
        counter = 0 
        while (counter != index):
            current_node = current_node.next 
            counter += 1
        
        return current_node





my_doubly_linked_list =  doubly_linked_list()

my_doubly_linked_list.append(5)
print(my_doubly_linked_list.print_list())
my_doubly_linked_list.append(6)
print(my_doubly_linked_list.print_list())


my_doubly_linked_list.prepend(7)
print(my_doubly_linked_list.print_list())
my_doubly_linked_list.prepend(4)
print(my_doubly_linked_list.print_list())


my_doubly_linked_list.insert(2, 99)
print(my_doubly_linked_list.print_list())
my_doubly_linked_list.insert(0, 0)
print(my_doubly_linked_list.print_list())
my_doubly_linked_list.insert(10, 100)
print(my_doubly_linked_list.print_list())

my_doubly_linked_list.remove(0)
print(my_doubly_linked_list.print_list())
my_doubly_linked_list.remove(5)
print(my_doubly_linked_list.print_list())

print(my_doubly_linked_list.remove(20))






