class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small, big = float('inf'),float('inf')
        for i in nums:
            if small > i:
                small = i
            elif i > small and i > big:
                return True
            elif small < i:
                big = i
        
        return False
        