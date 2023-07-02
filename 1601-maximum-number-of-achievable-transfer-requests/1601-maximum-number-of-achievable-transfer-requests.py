class Solution:
    def __init__(self):
        self.ans = 0
        self.requests = None
        self.transfers = [0]

    def maximumRequests(self, n, requests):
        self.requests,self.transfers = requests,self.transfers*n
        self.backTrack(0, 0)
        return self.ans

    def backTrack(self, index, count):
        if index == len(self.requests):
            if all(i == 0 for i in self.transfers):
                self.ans = max(self.ans, count)
            return
        
        self.transfers[self.requests[index][0]] -= 1
        self.transfers[self.requests[index][1]] += 1
        self.backTrack(index + 1, count + 1)
        
        self.transfers[self.requests[index][0]] += 1
        self.transfers[self.requests[index][1]] -= 1
        self.backTrack(index + 1, count)