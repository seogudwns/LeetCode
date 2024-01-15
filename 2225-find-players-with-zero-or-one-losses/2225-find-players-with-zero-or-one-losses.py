class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wincnt, losecnt = defaultdict(int), defaultdict(int)
        for i,j in matches:
            wincnt[i] += 1
            losecnt[j] += 1
        
        win, nex = set(), set()
        for i in set(wincnt.keys()).union(set(losecnt.keys())):
            if not losecnt[i]:
                win.add(i)
            elif losecnt[i] == 1:
                nex.add(i)
        
        return [sorted(win),sorted(nex)]