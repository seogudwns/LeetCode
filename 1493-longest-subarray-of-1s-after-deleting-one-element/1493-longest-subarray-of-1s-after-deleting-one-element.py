class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans,curr = [],0
        for i in nums:
            if i: curr+=i
            else:
                ans.append(curr)
                curr = 0
        if curr: ans.append(curr)
        print(ans)
        return ans[0]-1 if len(ans)==1 else max(sum(ans[i:i+2]) for i in range(len(ans)-1))