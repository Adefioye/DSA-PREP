# Hash implementation in python
class hash_table:
    def __init__(self, size):
        self.size = size 
        self.data = [None] * self.size 

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):
        hash = 0 
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size 

        return hash 

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []

        self.data[address].append([key, value])

        # return self.data

    def get(self, key):
        address = self._hash(key) 
        current_bucket = self.data[address] 

        if current_bucket:
            for item in current_bucket:
                if item[0] == key:
                    return item[1]

        return None

    def keys(self):
        keys_array = []
        for bucket in self.data:
            if bucket:
                for item in bucket:
                    keys_array.append(item[0])

        return keys_array

    def values(self):
        values_array = []
        for bucket in self.data:
            if bucket:
                for item in bucket:
                    values_array.append(item[1])

        return values_array





my_hash = hash_table(2)
print(my_hash.set("goat", 1)) 
print(my_hash.set("ape", 2)) 
print(my_hash.set("lion", 3)) 
print(my_hash.set("sheep", 4))
print(my_hash.get("goat"))
print(my_hash.get("lion"))
print(my_hash.get("tiger"))
print(my_hash.keys())
print(my_hash.values())
print(my_hash)

    
