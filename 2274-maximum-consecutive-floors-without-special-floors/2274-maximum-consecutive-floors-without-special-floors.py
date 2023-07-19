class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special = [bottom-1]+sorted(special)+[top+1]
        return max(special[i]-special[i-1] for i in range(1,len(special)))-1
        