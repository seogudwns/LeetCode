class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n,x = len(nums),defaultdict(int)
        curr,ans = 0,0
        l,r = 0,0
        while l<n:
            if r<n and x[nums[r]]<k:
                x[nums[r]]+=1
                r += 1
                curr += 1
                ans = max(curr,ans)
            else:
                x[nums[l]]-=1
                l += 1
                curr -= 1
        
        return ans