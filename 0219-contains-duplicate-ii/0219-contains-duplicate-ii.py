class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in dic:
                dic[num] = i
            else:
                if i-dic[num]<=k:
                    return True
                else:
                    dic[num] = i
                    
        return False