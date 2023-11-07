class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        tmp = sorted([dist[i] / speed[i] for i in range(len(dist))])
        
        for i in range(len(tmp)):
            if tmp[i] <= i: return i

        return len(dist)