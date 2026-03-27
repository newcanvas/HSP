import unittest

from task9 import NativeDictionary
from task9_2 import OrderedNativeDictionary, BitNativeDictionary

class DivTests(unittest.TestCase):

    # 4.

    def test_nd_put_get(self):
        ND = NativeDictionary(17, 2)
        self.assertIsNone(ND.get('key1'))
        ND.put('key1', 'первое значение')
        self.assertEqual(ND.get('key1'), 'первое значение')
        ND.put('key1', 'поменяли первое значение')
        self.assertEqual(ND.get('key1'), 'поменяли первое значение')

    def test_nd_is_key(self):
        ND = NativeDictionary(17, 2)
        self.assertFalse(ND.is_key('key1'))
        ND.put('key1', 'первое значение')
        self.assertTrue(ND.is_key('key1'))
        ND.put('key1', 'поменяли первое значение')
        self.assertTrue(ND.is_key('key1'))

    # 5.

    def test_ond_put_and_get(self):
        od = OrderedNativeDictionary(17, 2)
        self.assertIsNone(od.get('key1'))
        od.put('key1', 'первое значение')
        self.assertEqual(od.get('key1'), 'первое значение')
        od.put('key1', 'поменяли первое значение')
        self.assertEqual(od.get('key1'), 'поменяли первое значение')
        self.assertEqual(od.keys.len(), 1)

    def test_ond_delete(self):
        od = OrderedNativeDictionary(17, 2)
        od.delete('key1')
        od.put('key1', 'первое значение')
        od.put('key2', 'второе значение')
        od.put('key3', 'третье значение')
        od.delete('key2')
        self.assertIsNone(od.get('key2'))
        self.assertEqual(od.get('key1'), 'первое значение')
        self.assertEqual(od.keys.len(), 2)

    def test_ond_get_by_index(self):
        od = OrderedNativeDictionary(17, 2)
        self.assertIsNone(od.get_by_index(0))
        od.put('ключ3', 'третье значение')
        od.put('ключ1', 'первое значение')
        od.put('ключ2', 'второе значение')
        self.assertEqual(od.get_by_index(0), ('ключ1', 'первое значение'))
        self.assertEqual(od.get_by_index(2), ('ключ3', 'третье значение'))
        self.assertIsNone(od.get_by_index(3))

    def test_ond_descending_order(self):
        od = OrderedNativeDictionary(17, 2, asc=False)
        od.put('ключ1', 'первое значение')
        od.put('ключ2', 'второе значение')
        od.put('ключ3', 'третье значение')
        keys = [node.value for node in od.keys.get_all()]
        self.assertEqual(keys, ['ключ3', 'ключ2', 'ключ1'])
        self.assertEqual(od.get_by_index(0), ('ключ3', 'третье значение'))

    # 6.

    def test_bnd_put_get(self):
        bd = BitNativeDictionary(4)
        self.assertIsNone(bd.get('1011'))
        bd.put('1011', 'первое значение')
        self.assertEqual(bd.get('1011'), 'первое значение')
        bd.put('1011', 'поменяли первое значение')
        self.assertEqual(bd.get('1011'), 'поменяли первое значение')

    def test_bnd_delete(self):
        bd = BitNativeDictionary(4)
        bd.delete('1011')
        bd.put('1011', 'первое значение')
        bd.put('0001', 'второе значение')
        bd.delete('1011')
        self.assertIsNone(bd.get('1011'))
        self.assertFalse(bd.is_key('1011'))
        self.assertEqual(bd.get('0001'), 'второе значение')

    def test_bnd_boundary_keys(self):
        bd = BitNativeDictionary(4)
        bd.put('0000', 'нулевой ключ')
        bd.put('1111', 'максимальный ключ')
        self.assertEqual(bd.get('0000'), 'нулевой ключ')
        self.assertEqual(bd.get('1111'), 'максимальный ключ')
        bd.delete('0000')
        self.assertIsNone(bd.get('0000'))
        self.assertTrue(bd.is_key('1111'))

if __name__ == '__main__':
    unittest.main()
