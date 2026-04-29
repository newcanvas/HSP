class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        byte_sum = sum(key.encode('utf-8'))
        return byte_sum % self.size

    def is_key(self, key):
        slot = self.hash_fun(key)
        checked = 0
        while checked < self.size:
            if self.slots[slot] is None:
                return False
            if self.slots[slot] == key:
                return True
            slot += 1
            if slot >= self.size:
                slot -= self.size
            checked += 1
        return False

    def seek_slot(self, key):
        slot = self.hash_fun(key)
        checked = 0
        while checked < self.size:
            if self.slots[slot] is None or self.slots[slot] == key:
                return slot
            slot += 1
            if slot >= self.size:
                slot -= self.size
            checked += 1
        return None

    def put(self, key, value):
        slot = self.seek_slot(key)
        if slot is not None:
            self.slots[slot] = key
            self.values[slot] = value
            self.hits[slot] = 0
            return slot
        min_hits = min(self.hits)
        slot = self.hits.index(min_hits)
        self.slots[slot] = key
        self.values[slot] = value
        self.hits[slot] = 0
        return slot

    def get(self, key):
        slot = self.hash_fun(key)
        checked = 0
        while checked < self.size:
            if self.slots[slot] is None:
                return None
            if self.slots[slot] == key:
                self.hits[slot] += 1
                return self.values[slot]
            slot = (slot + 1) % self.size
            checked += 1
        return None

    def remove(self, key):
        slot = self.hash_fun(key)
        checked = 0
        while checked < self.size:
            if self.slots[slot] is None:
                return
            if self.slots[slot] == key:
                self.slots[slot] = None
                self.values[slot] = None
                self.hits[slot] = 0
                return
            slot += 1
            if slot >= self.size:
                slot -= self.size
            checked += 1
            
