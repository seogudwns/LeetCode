class Solution:
    def chk(self,idx,curr):
        if idx == self.n:
            self.ans.append(' '.join(self.wordDict[i] for i in curr))
            return
        
        for i,j in enumerate(self.wordDict):
            if self.s[idx:min(self.n,idx+len(j))] == j:
                self.chk(idx+len(j),curr+[i])
        
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ans = []
        self.s,self.n = s,len(s)
        self.wordDict,self.m = wordDict,len(wordDict)
        
        self.chk(0,[])
        
        return self.ans