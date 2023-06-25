class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(curr: int, remaining_fuel: int) -> int:
            if remaining_fuel < 0: return 0
            
            result = 1 if curr == finish else 0
            
            for next_loc in range(len(locations)):
                    
                if curr != next_loc:
                    cost = abs(locations[curr] - locations[next_loc])
                    result += dfs(next_loc, remaining_fuel - cost)
            return result % 1000000007
        
        return dfs(start, fuel)