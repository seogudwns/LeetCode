class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dic = defaultdict(list)
        for i,j,k in roads:
            dic[i].append((j,k))
            dic[j].append((i,k))
        ans = float('inf')
        Q = deque([1])
        while Q:
            x = Q.popleft()
            while dic[x]:
                y,val = dic[x].pop()
                ans = min(ans,val)
                Q.append(y)
        
        return ans