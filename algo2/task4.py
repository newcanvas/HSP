class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None

class BSTFind:

    def __init__(self):
        self.Node = None

        self.NodeHasKey = False
        self.ToLeft = False


class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size # массив ключей
	
    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        index = 0

        while index < len(self.Tree):
            if self.Tree[index] is None:
                return -index
            if key == self.Tree[index]:
                return index
            if key < self.Tree[index]:
                index = 2 * index + 1
            else:
                index = 2 * index + 2

        return None # не найден
	
    def AddKey(self, key):
        add_index = self.FindKeyIndex(key)
        if add_index is None:
            return -1
        if add_index < 0:
            self.Tree[-add_index] = key
            return -add_index
        if add_index == 0:
            self.Tree[0] = key
            return add_index
        # добавляем ключ в массив
        return add_index
        # индекс добавленного/существующего ключа или -1 если не удалось

