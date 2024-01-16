import random
class RandomizedSet(object):
    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_to_index:
            return False

        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val_to_index:
            return False

        index = self.val_to_index[val]
        last_val = self.values[-1]

        self.val_to_index[last_val] = index
        self.values[index] = last_val

        del self.val_to_index[val]
        self.values.pop()

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
