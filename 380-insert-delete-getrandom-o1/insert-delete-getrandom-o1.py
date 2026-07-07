import random

class RandomizedSet:

    def __init__(self):

        self.nums = []
        self.index = {}

    def insert(self, val: int) -> bool:

        if val in self.index:
            return False

        self.nums.append(val)
        self.index[val] = len(self.nums) - 1

        return True

    def remove(self, val: int) -> bool:

        if val not in self.index:
            return False

        remove_index = self.index[val]
        last_value = self.nums[-1]

        self.nums[remove_index] = last_value
        self.index[last_value] = remove_index

        self.nums.pop()
        del self.index[val]

        return True

    def getRandom(self) -> int:

        return random.choice(self.nums)