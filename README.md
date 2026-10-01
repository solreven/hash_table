# Hash Table Implementation Lab

`This summary is AI generated`

A Python implementation of a customized Hash Table data structure using a sum-of-Unicode hashing algorithm and separate chaining collision handling via dictionary nesting.

---

## Hashing Algorithm Overview

For the purpose of this lab, the hashing function computes a hash value by summing the Unicode (`ord()`) values of each character in the provided string key.

- The computed integer hash value serves as the top-level key inside the `collection` dictionary.
- To handle collisions (when different keys produce the same hash value), key-value pairs sharing the same hash are stored together inside a nested dictionary at that hash key.
- The same computed hash is used across all lookup, deletion, and insertion operations.

---

## Objective

Fulfill the user stories below and ensure all unit tests pass to complete the lab.

---

## User Stories

### 1. Initialization

- Define a class named `HashTable`.
- When a new instance of `HashTable` is created, its `collection` attribute must be initialized to an empty dictionary (`{}`).

### 2. Class Methods

The `HashTable` class must implement the following four instance methods:

#### `hash(self, key: str) -> int`

- Accepts a string `key` as a parameter.
- Returns an integer hash value computed as the sum of the Unicode values (`ord()`) of each character in the string.

#### `add(self, key: str, value: Any) -> None`

- Takes two arguments representing a `key`-`value` pair and computes the hash of the `key`.
- Uses the computed hash value as a top-level key in `collection` to store a nested dictionary containing the `key: value` pair.
- **Collision Handling:** If multiple keys produce the same hash value, append/update their key-value pairs inside the existing nested dictionary under that shared hash key.

#### `remove(self, key: str) -> None`

- Takes a `key` as its argument and computes its hash.
- Confirms whether the `key` exists within the hash table.
- Removes the corresponding key-value pair from the nested dictionary.
- If the key does not exist in the collection, it should handle it gracefully without raising an error or removing any data.

#### `lookup(self, key: str) -> Any`

- Takes a `key` as its argument and computes its hash.
- Searches the hash table and returns the associated `value` for that key.
- Returns `None` if the key does not exist in the collection.
