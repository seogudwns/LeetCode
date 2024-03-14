class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        summ = [0]
        for i in nums:
            summ.append(summ[-1]+i)
        
        curr = defaultdict(int)
        curr[summ[0]] = 1
        ans = 0
        for i in range(1,len(summ)):
            ans += curr[summ[i]-goal]
            curr[summ[i]] += 1
        
        return ans
        