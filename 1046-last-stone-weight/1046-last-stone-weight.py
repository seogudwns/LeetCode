class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)
        while True:
            if len(stones)<2: break
            x,y = -heapq.heappop(stones),-heapq.heappop(stones)
            if x == y: continue
            heapq.heappush(stones,y-x)
            
        return -sum(stones)