class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums = sorted(nums)
        leng = len(nums)
        # Initialize variables to keep track of unique elements and minimum operations.
        unique_len = 1
        ans = leng
        
        # Traverse the sorted list to remove duplicates and count unique elements.
        for i in range(1, leng):
            if nums[i] != nums[i - 1]:
                nums[unique_len] = nums[i]
                unique_len += 1
                
        # Initialize pointers for calculating operations within subarrays.
        i, j = 0, 0
        
        # Iterate over unique elements to find minimum operations.
        for i in range(unique_len):
            while j < unique_len and nums[j] - nums[i] <= leng - 1:
                j += 1
            ans = min(ans, leng - (j - i))
        
        return ans
