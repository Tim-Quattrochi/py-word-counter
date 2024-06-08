import unittest
from hash_class import MyHashTable


class TestMyHashTable(unittest.TestCase):
    def test_insert_and_get_value(self):

        hash_table = MyHashTable()

        # insert
        hash_table.insert("hello world", 5)
        hash_table.insert("python", 10)
        hash_table.insert("tensorflow", 15)

        # assertions
        self.assertEqual(hash_table.get_value("hello world"), 5)
        self.assertEqual(hash_table.get_value("python"), 10)
        self.assertEqual(hash_table.get_value("tensorflow"), 15)


if __name__ == '__main__':
    unittest.main()
