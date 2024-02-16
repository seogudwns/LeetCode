class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        x = Counter(arr)
        y = sorted(x,key = lambda z: -x[z])
        while y:
            w = y.pop()
            if x[w]<=k:
                k -= x[w]
                del x[w]
            else:
                return len(x)
        return 0