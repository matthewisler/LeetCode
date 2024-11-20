class RandomizedSet(object):

    def __init__(self):
        self.my_set = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.my_set:
            self.my_set.add(val)
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.my_set:
            self.my_set.remove(val)
            return True

        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        import random
        return random.choice(list(self.my_set))       


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()