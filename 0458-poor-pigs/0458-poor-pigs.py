class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1: return 0
        max_time = minutesToTest / minutesToDie + 1
        req_pigs = 1
        
        while max_time**req_pigs < buckets:
            req_pigs += 1

        return req_pigs