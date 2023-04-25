class SmallestInfiniteSet:

    def __init__(self):
        self.lst = [i for i in range(1,1001)]
        heapq.heapify(self.lst)

    def popSmallest(self) -> int:
        return heapq.heappop(self.lst)

    def addBack(self, num: int) -> None:
        if num not in self.lst: heapq.heappush(self.lst,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)