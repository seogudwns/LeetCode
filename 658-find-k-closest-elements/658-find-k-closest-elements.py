class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if max(arr)<=x:
            return arr[-k:]
        elif min(arr)>=x:
            return arr[:k]
        
        return sorted(sorted(arr,key = lambda y: abs(y-x))[:k])