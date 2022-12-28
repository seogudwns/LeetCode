class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles]
        heapq.heapify(piles)
        # print(piles)
        for i in range(k):
            heapq.heappush(piles,-((-heapq.heappop(piles)+1)//2))
        return -sum(piles)