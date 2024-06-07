from hash_class import MyHashTable
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


def main():
    hash_table = MyHashTable(20)
    hash_table.insert("hello", "there")
    print(hash_table.get_value("hello"))
    # hash_table.delete("hello")
    print(hash_table)


if __name__ == "__main__":
    main()
