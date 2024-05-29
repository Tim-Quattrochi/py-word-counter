# Reference slides: https://docs.google.com/presentation/d/14N_E4uZL6XqT4bejTkRYDq7sps-hBxN8VQTGXJCpGxg/edit#slide=id.p

# 1. Implement a hash function.
# - def hashcode(arg: string) -> int

# 2. Implement a hash table with chaining
# - insert(key, value)
# - lookup(key) -> value
# - delete(key)
# __len__ () => int
# - resize(int)
# - items() -> list or generator of [key, value] pairs

# 3. Use hash table to count word frequencies in a book.

# djb2 hash function implementation.
def djb2(key):
    hash_value = 5381
    for char in key:
        # "<<" bitwise left shift operator. It shifts the bits of its left-hand operand to the left by the number of positions specified by its right-hand operand.
        # "ord()" returns the Unicode code point for a given character.
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    # '&' is used for bitwise operations, 'and' is for logical.
    return hash_value & 0xFFFFFFFF


class MyHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        hash_value = self._hash(key)
        idx = hash_value % len(self.table)

        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] = value
                return
            # not found, add it.
        self.table[idx].append([key, value])

    def _hash(self, key):
        return djb2(key)

    # method for inspecting table.
    def __str__(self):
        return str(self.table)


hash_table = MyHashTable(20)

insert = hash_table.insert("hello", "there")


print(hash_table)
