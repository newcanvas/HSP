import unittest
from task12 import NativeCache

class DivTests(unittest.TestCase):

    def test_put_and_get_hits(self):
        cache = NativeCache(3)
        cache.put("a", 1)
        cache.put("b", 2)
        result = cache.get("a")
        self.assertEqual(result, 1)
        result = cache.get("a")
        self.assertEqual(result, 1)
        result = cache.get("b")
        self.assertEqual(result, 2)
        self.assertEqual(cache.hits[cache.seek_slot("a")], 2)
        self.assertEqual(cache.hits[cache.seek_slot("b")], 1)


    def test_min_hits(self):
        cache = NativeCache(3)
        cache.put("a", 1)
        cache.put("d", 2)
        cache.put("g", 3)
        cache.get("a")
        cache.get("a")
        cache.get("d")
        cache.put("j", 4)
        self.assertEqual(cache.is_key("a"), True)
        self.assertEqual(cache.is_key("d"), True)
        self.assertEqual(cache.is_key("g"), False)
        self.assertEqual(cache.get("j"), 4)


    def test_remove_resets_hits(self):
        cache = NativeCache(3)
        cache.put("a", 1)
        cache.get("a")
        cache.get("a")
        slot = cache.seek_slot("a")
        self.assertEqual(cache.hits[slot], 2)
        cache.remove("a")
        self.assertEqual(cache.is_key("a"), False)
        self.assertEqual(cache.hits[slot], 0)


    def test_overwrite_existing_key(self):
        cache = NativeCache(3)
        cache.put("a", 1)
        cache.get("a")
        cache.put("a", 100)
        result = cache.get("a")
        self.assertEqual(result, 100)
        self.assertEqual(cache.hits[cache.seek_slot("a")], 1)

if __name__ == '__main__':
    unittest.main()
