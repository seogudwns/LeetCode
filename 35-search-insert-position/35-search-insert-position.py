class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        if nums[0] == target:
            return 0
        elif nums[-1] == target:
            return right
        
        while True:
            print(left,right)
            if left == right:
                return left+1 if nums[left]<target else left
            
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid
            
            