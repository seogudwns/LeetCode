class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr[:] = arr[::-1]
        ans = 0
        while k:
            ans += 1
            if arr and arr[-1] == ans: arr.pop()
            else: k -= 1
        
        return ans