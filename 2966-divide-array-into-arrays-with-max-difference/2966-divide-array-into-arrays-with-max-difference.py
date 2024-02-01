class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums = sorted(nums,reverse=True)
        ans = []
        curr_list = []
        while nums:
            curr_elt = nums.pop()
            if not curr_list:
                curr_list.append(curr_elt)
            elif curr_elt-curr_list[0]>k:
                return []
            else: curr_list.append(curr_elt)
            
            if len(curr_list) == 3:
                ans.append(curr_list)
                curr_list = []
        
        return ans