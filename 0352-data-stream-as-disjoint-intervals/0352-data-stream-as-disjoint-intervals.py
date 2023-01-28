class SummaryRanges:

    def __init__(self):
        self.arr = []

    def addNum(self, value: int) -> None:
        start,end,idx = 0,len(self.arr),0
        while start<end:
            mid = (start+end)//2
            l,r = self.arr[mid]
            if l<=value<=r:
                return
            elif value > r:
                idx = start = mid+1
            else:
                idx = end = mid
                
        if idx == len(self.arr):
            if len(self.arr) and self.arr[-1][1] + 1 == value:
                self.arr[-1][1] = value
            else: 
                self.arr.append([value, value])
        elif idx >= 0:
            if self.arr[idx][0]-1 == value:    
                self.arr[idx][0] = value
                if idx and self.arr[idx-1][1] + 1 == self.arr[idx][0]:
                    self.arr[idx-1][1] = self.arr[idx][1]
                    del self.arr[idx]
            elif idx and self.arr[idx-1][1]+1 == value:
                self.arr[idx-1][1] = value  
            else:
                self.arr.insert(idx, [value, value])
        
    def getIntervals(self) -> List[List[int]]:
        return self.arr

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()