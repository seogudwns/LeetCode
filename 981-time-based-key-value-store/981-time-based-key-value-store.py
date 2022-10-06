

class TimeMap:

    def __init__(self):
        self.Tdict = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.Tdict:
            self.Tdict[key] = dict()
        
        self.Tdict[key][timestamp] = value
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.Tdict:
            return ''
        
        for ts in range(timestamp, 0, -1):
            if ts in self.Tdict[key]:
                return self.Tdict[key][ts]
        
        return ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)