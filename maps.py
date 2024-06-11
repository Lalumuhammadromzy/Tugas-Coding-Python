class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

# Penggunaan
ht = HashTable()
ht.insert('a', 1)
ht.insert('b', 2)
print(ht.get('a'))  # Output: 1
print(ht.get('b'))  # Output: 2
print(ht.get('c'))  # Output: None
