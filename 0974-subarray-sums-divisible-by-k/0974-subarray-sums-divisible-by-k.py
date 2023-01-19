class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # TLE
        prefs = defaultdict(int)
        prefs[0] = 1
        res,calc = 0,0

        for i in nums:
            calc = (calc+i)%k    
            res += prefs[calc]
            prefs[calc] += 1
        
        return res
            
        
        
        