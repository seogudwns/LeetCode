class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        right = len(nums)
        left = 0
        if nums[-1] < target:
            return -1
        
        while True:
            if right == left:
                return -1
            
            mid = (right+left)//2
            curr = nums[mid]
            if curr == target:
                return mid
            elif curr > target:
                right = mid
            elif curr < target:
                if nums[mid+1] > target:
                    return -1
                
                left = mid + 1
        
        