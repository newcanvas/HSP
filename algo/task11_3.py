import unittest
from task11 import BloomFilter
from task11_2 import CountingBloomFilter

class TestBloomFilter(unittest.TestCase):

    # 1.

    def test_add_and_check(self):
        bf = BloomFilter(32)

        strings = [
            "0123456789",
            "1234567890",
            "2345678901",
            "3456789012",
            "4567890123",
            "5678901234",
            "6789012345",
            "7890123456",
            "8901234567",
            "9012345678"]

        for s in strings:
            bf.add(s)

        for s in strings:
            self.assertEqual(bf.is_value(s), True)

    def test_empty_filter(self):
        bf = BloomFilter(32)
        self.assertEqual(bf.is_value("test"), False)
        self.assertEqual(bf.bits, 0)

    def test_not_existing_element(self):
        bf = BloomFilter(32)
        bf.add("0123456789")
        bf.add("1234567890")
        result = bf.is_value("not_present")
        self.assertIn(result, [True, False])

    def test_bit_changes(self):
        bf = BloomFilter(32)
        self.assertEqual(bf.bits, 0)
        bf.add("0123456789")
        first_state = bf.bits
        self.assertNotEqual(first_state, 0)
        bf.add("1234567890")
        second_state = bf.bits
        self.assertNotEqual(first_state, second_state)

    def test_idempotent_add(self):
        bf = BloomFilter(32)
        bf.add("0123456789")
        state1 = bf.bits
        bf.add("0123456789")
        state2 = bf.bits
        self.assertEqual(state1, state2)

    # 2.

    def test_merge_basic(self):
        bf1 = BloomFilter(32)
        bf2 = BloomFilter(32)
        bf1.add("0123456789")
        bf2.add("1234567890")
        merged = bf1.merge_filters(bf2)
        self.assertEqual(merged.is_value("0123456789"), True)
        self.assertEqual(merged.is_value("1234567890"), True)

    def test_merge_no_change(self):
        bf1 = BloomFilter(32)
        bf2 = BloomFilter(32)
        bf1.add("0123456789")
        bf2.add("1234567890")
        bits1_before = bf1.bits
        bits2_before = bf2.bits
        merged = bf1.merge_filters(bf2)
        self.assertEqual(bf1.bits, bits1_before)
        self.assertEqual(bf2.bits, bits2_before)
        self.assertNotEqual(merged.bits, bf1.bits)

    def test_merge_empty_filter(self):
        bf1 = BloomFilter(32)
        bf2 = BloomFilter(32)
        bf1.add("0123456789")
        empty = BloomFilter(32)
        merged = bf1.merge_filters(empty)
        self.assertEqual(merged.is_value("0123456789"), True)
        self.assertEqual(merged.bits, bf1.bits)

    def test_merge_idempotent(self):
        bf1 = BloomFilter(32)
        bf2 = BloomFilter(32)
        bf1.add("0123456789")
        bf2.add("1234567890")
        merged1 = bf1.merge_filters(bf2)
        merged2 = bf1.merge_filters(bf2)
        self.assertEqual(merged1.bits, merged2.bits)

    # 3.

    def test_add_and_check2(self):
        bf = CountingBloomFilter(32)

        strings = [
            "0123456789",
            "1234567890",
            "2345678901",
            "3456789012",
            "4567890123",
            "5678901234",
            "6789012345",
            "7890123456",
            "8901234567",
            "9012345678"]

        for s in strings:
            bf.add(s)

        for s in strings:
            self.assertEqual(bf.is_value(s), True)

    def test_remove_existing(self):
        bf = CountingBloomFilter(32)
        bf.add("0123456789")
        self.assertEqual(bf.is_value("0123456789"), True)
        bf.remove("0123456789")
        self.assertEqual(bf.is_value("0123456789"), False)

    def test_remove_non_existing(self):
        bf = CountingBloomFilter(32)
        bf.add("0123456789")
        bf.remove("not_present")
        self.assertEqual(bf.is_value("0123456789"), True)

    def test_double_remove(self):
        bf = CountingBloomFilter(32)
        bf.add("0123456789")
        bf.remove("0123456789")
        bf.remove("0123456789")
        self.assertEqual(bf.is_value("0123456789"), False)
        self.assertTrue(all(x >= 0 for x in bf.bits))

    # 4.

    def test_recover_basic(self):
        bf = BloomFilter(32)
        data = ["0123456789", "1234567890", "2345678901"]
        for s in data:
            bf.add(s)
        candidates = data + ["not_present", "0000000000"]
        result = bf.recover(candidates)
        for s in data:
            self.assertIn(s, result)

    def test_recover_empty_filter(self):
        bf = BloomFilter(32)
        candidates = ["0123456789","1234567890"]
        result = bf.recover(candidates)
        self.assertEqual(result, [])

    def test_recover_all_candidates(self):
        bf = BloomFilter(32)
        candidates = ["0123456789","1234567890","2345678901","3456789012"]
        for s in candidates:
            bf.add(s)
        result = bf.recover(candidates)
        self.assertEqual(set(result), set(candidates))

if __name__ == '__main__':
    unittest.main()
