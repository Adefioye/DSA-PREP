class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def push(self, item):
        self.length += 1
        self.data[self.length - 1] = item
        return self.data 

    def delete(self, index):
        deleted_item = self.data[index]
        del self.data[index]
        self.length -= 1
        self.shift_items(index)
        del self.data[self.length]
        return (deleted_item, self.data)

    def shift_items(self, index):
        for i in range(index, self.length):
            self.data[i] = self.data[i + 1]

    def insert(self, index, item):
        for i in range(index+1, self.length+1):
            self.data[i] = self.data[i - 1]

        self.data[index] = item 
        self.length += 1 
        return self.data




newArray = MyArray()
# print(newArray.get(0))
print(newArray.push("Hi!"))
print(newArray.push("Cokesman"))
print(newArray.push("MB"))
print(newArray.push("BJ"))
print(newArray.push("You"))
print(newArray.push("are"))
print(newArray.push("awesome"))
print(newArray.pop())
print(newArray.pop())
print(newArray.delete(2))
print(newArray.insert(3, "Ishow"))



