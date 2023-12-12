class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr)
        qtr = size // 4
        x = Counter(arr)
        
        for i in x:
            if x[i]>qtr:
                return i