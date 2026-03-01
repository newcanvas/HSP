import unittest

from task8 import HashTable
from task8_2 import HashTable2, generate_ddos_keys, HashTableSalted, HashTableTwoFun

class DivTests(unittest.TestCase):

    def test_put_empty_table(self):
        ht = HashTable(17, 3)
        result = ht.put("a")
        self.assertEqual(result, ht.find("a"))

    def test_find_empty_table(self):
        ht = HashTable(17, 3)
        self.assertIsNone(ht.find("a"))

    def test_seek_slot_collision(self):
        ht = HashTable(17, 3)
        result1 = ht.put("a")
        result2 = ht.put("a")
        self.assertEqual(result2, result1 + 3)

    def test_seek_slot_wrap_around(self):
        ht = HashTable(3, 1)
        ht.put("a")
        ht.put("b")
        slot = ht.seek_slot("c")
        self.assertIsNotNone(slot)

    def test_seek_slot_full_table(self):
        ht = HashTable(3, 1)
        ht.put("a")
        ht.put("b")
        ht.put("c")
        self.assertIsNone(ht.seek_slot("d"))

    def test_find(self):
        ht = HashTable(5, 1)
        self.assertIsNone(ht.find("a"))
        ht.put("a")
        slot = ht.find("a")
        self.assertIsNotNone(slot)
        self.assertIsNone(ht.find("b"))

    # 3.

    def test_put_empty_table_2(self):
        ht = HashTable2(17, 3)
        result = ht.put("a")
        self.assertEqual(result, ht.find("a"))
        self.assertEqual(ht.capacity, 1)
        self.assertEqual(ht.size, 17)

    def test_resize_table(self):
        ht = HashTable2(17, 3)
        for i in range(20):
            ht.put(str(i))
        self.assertEqual(ht.capacity, 20)
        self.assertEqual(ht.size, 34)

    def test_seek_slot_full_table_2(self):
        ht = HashTable2(3, 1)
        ht.put("a")
        ht.put("b")
        ht.put("c")
        self.assertIsNone(ht.seek_slot("d"))

    def test_find_2(self):
        ht = HashTable2(17, 3)
        for i in range(20):
            ht.put(str(i))
        self.assertIsNone(ht.find("a"))
        ht.put("a")
        slot = ht.find("a")
        self.assertIsNotNone(slot)
        self.assertIsNone(ht.find("b"))

    # 4.

    def test_put_empty_table_two(self):
        ht = HashTableTwoFun(17, 3)
        result = ht.put("a")
        self.assertEqual(result, ht.find("a"))

    def test_find_empty_table_two(self):
        ht = HashTableTwoFun(17, 3)
        self.assertIsNone(ht.find("a"))

    def test_seek_slot_wrap_around_two(self):
        ht = HashTableTwoFun(3, 1)
        ht.put("a")
        ht.put("b")
        slot = ht.seek_slot("c")
        self.assertIsNotNone(slot)

    def test_seek_slot_full_table_two(self):
        ht = HashTableTwoFun(3, 1)
        ht.put("a")
        ht.put("b")
        ht.put("c")
        self.assertIsNone(ht.seek_slot("d"))

    def test_find_two(self):
        ht = HashTableTwoFun(5, 1)
        self.assertIsNone(ht.find("a"))
        ht.put("a")
        slot = ht.find("a")
        self.assertIsNotNone(slot)
        self.assertIsNone(ht.find("b"))

    # 5.

    def test_ddos_same_hash_mod(self):
        ht = HashTable(3, 1)
        keys = generate_ddos_keys(3, 0)
        for i in range(len(keys)):
            self.assertEqual(ht.seek_slot(keys[i]), i)
            ht.put(keys[i])

    def test_ddos_same_hash_mod_2(self):
        ht = HashTable(17, 1)
        keys = generate_ddos_keys(17, 0)
        for i in range(len(keys)):
            self.assertEqual(ht.seek_slot(keys[i]), i)
            ht.put(keys[i])

    def test_put_empty_table_salted(self):
        ht = HashTableSalted(17, 3)
        result = ht.put("a")
        self.assertEqual(result, ht.find("a"))

    def test_ddos_same_hash_with_salt(self):
        ht = HashTableSalted(17, 1)
        keys = generate_ddos_keys(17, 0)
        counter = 0
        for i in range(len(keys)):
            if ht.seek_slot(keys[i]) == i:
                counter += 1
        self.assertNotEqual(counter, ht.size)

if __name__ == '__main__':
    unittest.main()
