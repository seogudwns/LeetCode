class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k==1: return 0
        arr = sorted(map(sum,(pairwise(weights))))
        # print(arr,list(pairwise(weights)))
        return  sum(arr[-k+1:]) - sum(arr[:k-1]) 
    