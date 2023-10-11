class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        tsum = []
        while flowers:
            x,y = flowers.pop()
            heapq.heappush(tsum,(x-1,1))
            heapq.heappush(tsum,(y,-1))
            
        pset = list(set(people))
        heapq.heapify(pset)
        
        res = {}
        curr = 0
        while pset:
            if not tsum:
                for i in pset:
                    res[i] = 0
                break
                    
            if tsum[0][0]<pset[0]:
                curr+=heapq.heappop(tsum)[1]
            else:
                res[heapq.heappop(pset)] = curr
        
        return [res[i] for i in people]