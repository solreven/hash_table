class HashTable:
    def __init__(self):
        collection = {}

    def hash(self, string: str) -> int:
        to_hash = string
        hashed = 0
        for letter in to_hash:
            hashed += ord(letter)
        return hashed

    def add(self, key: str, value: str):
        hashkey = self.hash(key)
        if hashkey not in self.collection:
            self.collection[hashkey] = {}
        self.collection[hashkey][key] = value

    def remove(self):
        pass
        
    def lookup(self):
        pass
