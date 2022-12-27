class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        remains = sorted([capacity[i]-rocks[i] for i in range(n)])
        curr = 0
        # print(remains,sum(remains))
        while curr != n:
            if not additionalRocks:
                break
            if additionalRocks > 0 and remains[curr]:
                if additionalRocks >= remains[curr]:
                    additionalRocks -= remains[curr]
                    remains[curr] = 0
                else:
                    break
            
            curr += 1
        
        return remains.count(0)