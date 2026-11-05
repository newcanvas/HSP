class Heap:

    def __init__(self):
        self.HeapArray = []

    def MakeHeap(self, a, depth):
        size = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * size

        for key in a:
            if not self.Add(key):
                break

    def GetMax(self):
        count = self._count()
        if count == 0:
            return -1

        result = self.HeapArray[0]
        last = count - 1

        self.HeapArray[0] = self.HeapArray[last]
        self.HeapArray[last] = None

        if last > 0:
            self._sift_down(0)

        return result

    def Add(self, key):
        count = self._count()
        if count == len(self.HeapArray):
            return False

        self.HeapArray[count] = key
        self._sift_up(count)

        return True

    def IsHeap(self):
        seen_empty = False

        for index, key in enumerate(self.HeapArray):
            if key is None:
                seen_empty = True
                continue

            if seen_empty:
                return False

            if index > 0 and self.HeapArray[(index - 1) // 2] < key:
                return False

        return True

    def _count(self):
        for index, key in enumerate(self.HeapArray):
            if key is None:
                return index

        return len(self.HeapArray)

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.HeapArray[parent] >= self.HeapArray[index]:
                break

            self._swap(parent, index)
            index = parent

    def _sift_down(self, index):
        size = len(self.HeapArray)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if (left < size and self.HeapArray[left] is not None and self.HeapArray[left] > self.HeapArray[largest]):
                largest = left

            if (right < size and self.HeapArray[right] is not None and self.HeapArray[right] > self.HeapArray[largest]):
                largest = right

            if largest == index:
                break

            self._swap(index, largest)
            index = largest

    def _swap(self, i, j):
        self.HeapArray[i], self.HeapArray[j] = self.HeapArray[j], self.HeapArray[i]
