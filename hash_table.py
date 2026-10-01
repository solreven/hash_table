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
        hashkey = self.hash(key)
        if hashkey not in self.collection or key not in self.collection[hashkey]:
            return None
        else:
            return self.collection[hashkey][key]


    '''Take a key as its argument.
Compute the hash of the key, and return the corresponding value stored inside the hash table.
If the key does not exist in the collection, it should return None.'''