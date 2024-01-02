class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        while nums:
            x = nums.pop()
            for i in range(len(ans)):
                if x not in ans[i]:
                    ans[i].add(x)
                    break
            else:
                ans.append({x})
        
        return ans