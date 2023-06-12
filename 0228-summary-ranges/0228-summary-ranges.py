class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        ans,idx,curr,stt = [],1,nums[0],nums[0]
        
        while idx<len(nums):
            curr = nums[idx]
            if nums[idx-1]+1 != curr:
                ans.append(str(stt) if stt == nums[idx-1] else f'{stt}->{nums[idx-1]}')
                stt = nums[idx]
                
            idx += 1
                    
        ans.append(str(stt) if stt == nums[idx-1] else f'{stt}->{nums[idx-1]}')
        
        return ans