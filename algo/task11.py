class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bits = 0

    def hash1(self, s):
        h = 0
        for ch in s:
            h = (h * 17 + ord(ch)) % self.size
        return h

    def hash2(self, s):
        h = 0
        for ch in s:
            h = (h * 223 + ord(ch)) % self.size
        return h

    def add(self, s):
        i1 = self.hash1(s)
        i2 = self.hash2(s)
        self.bits |= (1 << i1)
        self.bits |= (1 << i2)

    def is_value(self, s):
        i1 = self.hash1(s)
        i2 = self.hash2(s)
        if (self.bits & (1 << i1)) == 0:
            return False
        if (self.bits & (1 << i2)) == 0:
            return False
        return True

    def merge_filters(self, other):
        new_filter = BloomFilter(self.size)
        new_filter.bits = self.bits | other.bits
        return new_filter

    def recover(self, strings):
        result = []
        for i in strings:
            if self.is_value(i):
                result.append(i)
        return result



