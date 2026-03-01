class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        hash = sum(value.encode('utf-8'))
        index = hash % self.size
        return index

    def seek_slot(self, value):
        slot = self.hash_fun(value)
        if self.slots[slot] is None:
            return slot
        counter = set()
        while len(counter) < self.size:
            slot += self.step
            if slot > (self.size - 1):
                slot = slot - self.size
            if self.slots[slot] is None:
                return slot
            counter.add(slot)
            continue
        return None

    def put(self, value):
        slot = self.seek_slot(value)
        if slot is None:
            return None
        self.slots[slot] = value
        return slot

    def find(self, value):
        slot = self.hash_fun(value)
        if self.slots[slot] == value:
            return slot
        counter = set()
        while len(counter) < self.size:
            slot += self.step
            if slot > (self.size - 1):
                slot = slot - self.size
            if self.slots[slot] == value:
                return slot
            counter.add(slot)
            continue
        return None

