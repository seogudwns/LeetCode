class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        num,ans = deque([0]),10**5+1
        for i in range(len(nums)):
            num.append(nums[i]+num[-1] if num else nums[i])
            while num and num[-1]-num[0]>=target: 
                num.popleft()
                ans = min(ans,len(num))
                
        return ans if ans !=10**5+1 else 0