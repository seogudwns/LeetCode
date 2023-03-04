# class Solution:
#     def local(stt,end,hi,lo):
#         return 0
    
#     def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
#         self.nums,self.ans = nums,0
#         out,hi,lo = -1,[],[]
        
#         for i in range(len(self.nums)):
#             if self.nums[i] == minK: lo.append(i)
#             if self.nums[i] == maxK: hi.append(i)
            
#         return 1

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        minFound = False
        maxFound = False
        start = 0
        minStart = 0
        maxStart = 0
        for i in range(len(nums)):
            num = nums[i]
            if num < minK or num > maxK:
                minFound = False
                maxFound = False
                start = i+1
            if num == minK:
                minFound = True
                minStart = i
            if num == maxK:
                maxFound = True
                maxStart = i
            if minFound and maxFound:
                res += (min(minStart, maxStart) - start + 1)
        return res