from __future__ import annotations
from typing import Any

class PowerSet:

    def __init__(self) -> None:
        self.pow_set = []
        self.dict = {}

    def size(self) -> int:
        return len(self.pow_set)

    def put(self, value: Any) -> None:
        if value not in self.dict:
            self.pow_set.append(value)
            self.dict[value] = True
        return

    def get(self, value: Any) -> bool:
        return value in self.dict

    def remove(self, value: Any) -> bool:
        result = self.get(value)
        if result:
            self.pow_set.remove(value)
            del self.dict[value]
        return result

    def intersection(self, set2: PowerSet) -> PowerSet:
        inter = PowerSet()
        if self.size() < set2.size():
            min_s = self.dict
            max_s = set2.dict
        else:
            min_s = set2.dict
            max_s = self.dict

        for i in min_s:
            if i in max_s:
                inter.put(i)
        return inter

    def union(self, set2: PowerSet) -> PowerSet:
        uni = PowerSet()
        for i in self.dict:
            uni.put(i)
        for i in set2.dict:
            uni.put(i)
        return uni

    def difference(self, set2: PowerSet) -> PowerSet:
        diff = PowerSet()
        for i in self.dict:
            if i not in set2.dict:
                diff.put(i)
        return diff

    def issubset(self, set2: PowerSet) -> bool:
        for i in set2.dict:
            if i in self.dict:
                continue
            return False
        return True

    def equals(self, set2: PowerSet) -> bool:
        if self.size() != set2.size():
            return False
        for i in self.dict:
            if i in set2.dict:
                continue
            return False
        return True

