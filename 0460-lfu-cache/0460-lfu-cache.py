class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count
    
class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.key2node = {}
        self.count2node = defaultdict(OrderedDict)
        self.minCount = None
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1
        
        node = self.key2node[key]
        del self.count2node[node.count][key]
        
        # clean memory
        if not self.count2node[node.count]:
            del self.count2node[node.count]
        
        node.count += 1
        self.count2node[node.count][key] = node
        
        # NOTICE check minCount!!!
        if not self.count2node[self.minCount]:
            self.minCount += 1
            
            
        return node.val
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if not self.cap:
            return 
        
        if key in self.key2node:
            self.key2node[key].val = value
            self.get(key) # NOTICE, put makes count+1 too
            return
        
        if len(self.key2node) == self.cap:
            # popitem(last=False) is FIFO, like queue
            # it return key and value!!!
            k, n = self.count2node[self.minCount].popitem(last=False) 
            del self.key2node[k] 
        
        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return
    
# 뭐 이딴 문제가 다있냐.. 이해 안되서 일단 패스.
# class LFUCache:

#     def __init__(self, capacity: int):
#         self.cache = dict()
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if not self.capacity:
#             return -1
#         if key in self.cache:
#             self.cache[key]+=1
#             return self.cache[key]-1
        
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if not self.capacity:
#             return
        
#         if key not in self.cache:
#             if len(self.cache) == self.capacity:
#                 del self.cache[sorted(self.cache,key=lambda x: (self.cache[x],x))[0]]
#         self.cache[key]=value
        
#         return


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)