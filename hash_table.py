class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string: str) -> int:
        to_hash = string
        hashed = 0
        for letter in to_hash:
            hashed += ord(letter)
        return hashed

    def add(self, key: str, value: str) -> None:
        hashkey = self.hash(key)
        if hashkey not in self.collection:
            self.collection[hashkey] = {}
        self.collection[hashkey][key] = value

    def remove(self, key: str):
        hashkey = self.hash(key)
        if hashkey in self.collection and key in self.collection[hashkey]:    
            del self.collection[hashkey][key]
        else:
            return
        
    def lookup(self, key) -> str:
        pass


'''Take a key as its argument and compute its hash.
Confirm if the key exists in the collection.
Remove the corresponding key-value pair from the hash table.
If the key does not exist in the collection, it should not raise an error or remove anything.'''