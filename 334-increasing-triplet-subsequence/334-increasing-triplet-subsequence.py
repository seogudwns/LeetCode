class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
#         # basic code..
#         X = Counter(nums)
#         if len(X.keys()) < 3 or nums == sorted(nums,reverse=True):
#             return False
        
#         n = len(nums)
#         for i in range(n-2):
#             for j in range(i+1,n-1):
#                 if nums[i]<nums[j]:
#                     for k in range(j+1,n):
#                         if nums[j]<nums[k]:
#                             return True
#         return False
#         # 야 이게 통과가 되네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
        small, big = float('inf'),float('inf')
        for i in nums:
            if small > i:
                small = i
            elif i > small and i > big:
                return True
            elif small < i:
                big = i
        
        return False
        