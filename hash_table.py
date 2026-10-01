'''The collection dictionary should store key-value pairs based on the hashed value of the key.'''

class HashTable:
    def __init__(self):
        collection = {}

    def hash(self, string: str) -> int:
        to_hash = string
        hashed = 0
        for letter in to_hash:
            hashed += ord(letter)
        return hashed
    def add():
        pass
    def remove(self):
        pass
    def lookup(self):
        pass
