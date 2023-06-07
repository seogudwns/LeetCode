class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(100):
            num = 2**i
            if c&num:
                if a&num or b&num:
                    continue
                ans +=1
            else:
                if a&num: ans+=1
                if b&num: ans+=1
        
        return ans