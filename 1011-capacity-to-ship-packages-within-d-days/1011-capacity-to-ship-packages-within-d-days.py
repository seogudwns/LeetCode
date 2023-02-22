class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if len(weights)<=days: return max(weights)
        
        l,r = max(weights),sum(weights)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            if self.check(weights, days, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

    def check(self, weights: List[int], days: int, capacity: int) -> bool:
        required_days = 1
        curr_weight = 0
        for i in weights:
            if curr_weight + i > capacity:
                required_days += 1
                if required_days > days: return False
                
                curr_weight = 0
            curr_weight += i
        return True    
        
        
        
        