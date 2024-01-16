class RandomizedSet:

    def __init__(self):
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val in self.dic: return False
        self.dic[val] = 1
        return True

    def remove(self, val: int) -> bool:
        try:
            del self.dic[val]
            return True
        except:
            return False

    def getRandom(self) -> int:
        return list(self.dic)[0] if len(self.dic) == 1 else list(self.dic)[randint(0,len(self.dic)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()