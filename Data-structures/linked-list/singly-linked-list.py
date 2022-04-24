# 9 --> 10 --> 99 --> 5 --> 7

class singly_linked_list:
    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None
            }

        self.tail = self.head
        self.length = 1

    def __str__(self):
        return str(self.__dict__)

    def append(self, value):
        new_node = {
            "value": value,
            "next": None
        }
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = {
            "value": value,
            "next": None
        }
        new_node["next"] = self.head 
        self.head = new_node
        self.length += 1

    def print_values(self):
        value_array = []
        current_node = self.head 
        while (current_node != None):
            value_array.append(current_node.get("value"))
            current_node = current_node["next"]

        return value_array


    def insert(self, index, value):

        if (index > self.length):
            self.append(value)
        elif (index == 0):
            self.prepend(value)
        else:
            new_node = {
            "value": value,
            "next": None
            }

            leader_node = self.traverse_to_index(index - 1)
            follower_node = leader_node["next"]
            leader_node["next"] = new_node 
            new_node["next"] = follower_node 
            self.length += 1

    def remove(self, index):

        if (index == 0):
            self.head = self.head["next"]
            self.length -= 1
        elif (index == self.length - 1):
            leader_node = self.traverse_to_index(index - 1)
            leader_node["next"] = None 
            self.tail = leader_node 
            self.length -= 1
        else:
            leader_node = self.traverse_to_index(index - 1)
            unwanted_node = leader_node["next"]
            leader_node["next"] = unwanted_node["next"]
            self.length -= 1

    def traverse_to_index(self, index):
        current_node = self.head 
        counter = 0
        while (counter != index ):
            current_node = current_node["next"]
            counter += 1 
        
        return current_node

    def reverse(self):
        current_node = self.head 
        self.tail = self.head
        follower_node = current_node["next"]
        while follower_node:
            temp_node = follower_node["next"] 
            follower_node["next"] = current_node
            current_node = follower_node
            follower_node = temp_node

        self.head["next"] = None
        self.head = current_node

        return self
    




    

# 9 --> 10 --> 99 --> 5 --> 7

my_linked_list = singly_linked_list(10)
my_linked_list.append(5)
my_linked_list.prepend(9)
my_linked_list.insert(0, 99)
print(my_linked_list.print_values())
my_linked_list.insert(10, 55)
print(my_linked_list.print_values())
my_linked_list.insert(2, 90)
print(my_linked_list.print_values())
my_linked_list.remove(0)
print(my_linked_list.print_values())
my_linked_list.remove(4)
print(my_linked_list.print_values())
my_linked_list.remove(2)
print(my_linked_list.print_values())


my_linked_list.reverse()
print(my_linked_list.print_values())
