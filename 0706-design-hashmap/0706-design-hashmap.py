class MyHashMap:

    def __init__(self):
        self.map = []
    def chk(self,key):
        if key>len(self.map)-1: self.map += [-1]*(key+1-len(self.map))

    def put(self, key: int, value: int) -> None:
        self.chk(key)
        self.map[key] = value
        
    def get(self, key: int) -> int:
        self.chk(key)
        return self.map[key]
    
    def remove(self, key: int) -> None:
        self.chk(key)
        self.map[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)