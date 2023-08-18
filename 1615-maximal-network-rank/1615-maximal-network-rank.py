class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads: return 0
        gp = defaultdict(set)
        for i,j in roads:
            gp[i].add(j)
            gp[j].add(i)
            
        degdict = defaultdict(list)
        deg = set()
        for i in gp: 
            degdict[len(gp[i])].append(i)
            deg.add(len(gp[i]))
        
        candid = degdict[max(deg)]
        if len(deg)>1: deg.discard(max(deg)); candid+=degdict[max(deg)]
        
        ans = 0
        for i,j in permutations(candid,2):
            ans = max(ans,len(gp[i])+len(gp[j]) if i not in gp[j] else len(gp[i])+len(gp[j])-1)
        
        return ans