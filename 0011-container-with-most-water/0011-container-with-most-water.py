class Solution:
    def maxArea(self, height: List[int]) -> int:
#         # initial code.
#         leng = len(height)
#         result = 0
#         for i in range(leng-1):
#             for j in range(i+1,leng):
#                 water = min(height[i],height[j])*(j-i)
#                 if result<water:
#                     result = water
        
#         return result
        left,right = 0,len(height)-1
        result = 0
        while left<right:
            lh,rh = height[left],height[right]
            curr = min(lh,rh)*(right-left)
            if result < curr:
                result = curr
            
            if lh<rh:
                left += 1
            else:
                right -= 1
        
        return result
        
        
        