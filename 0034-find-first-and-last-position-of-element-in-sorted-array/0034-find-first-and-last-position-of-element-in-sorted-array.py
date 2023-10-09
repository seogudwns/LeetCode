class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        if not nums: return ans
        if nums[0] == target: 
            if len(nums)>1 and nums[1] > target: ans[1] = 0
            ans[0] = 0
        if nums[-1] == target: 
            if len(nums)>1 and nums[-2] < target: ans[0] = len(nums)-1
            ans[1] = len(nums)-1
        
        if ans[0] == -1:
            l,r = 0,len(nums)-1
            while l<r:
                mid = (l+r)//2
                if nums[mid-1] < target and nums[mid] == target:
                    ans[0] = mid
                    break
                elif nums[mid]<target:
                    l = mid+1
                else:
                    r = mid
        
        if ans[1] == -1:
            l,r = 0,len(nums)-1
            while l<r:
                mid = (l+r)//2
                if target < nums[mid+1] and nums[mid] == target:
                    ans[1] = mid
                    break
                elif nums[mid]>target:
                    r = mid
                else:
                    l = mid+1
        
        return ans