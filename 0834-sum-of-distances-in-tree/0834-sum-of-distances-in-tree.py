class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Others
        g = defaultdict(list)
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)
            
        ans = 0
        subtree = {}
        
        def dfs(node, prev, depth):
            total = 1
            nonlocal ans
            ans+=depth
            for child in g[node]:
                if child == prev:
                    continue
                total+=dfs(child, node, depth + 1)
            subtree[node] = total
            return total
        
        dfs(0, None, 0)
        res = [0] * n
        res[0] = ans
        # print(ans,subtree)
        def dfs2(node, prev):
            for child in g[node]:
                if child == prev:
                    continue
                res[child] = res[node] - subtree[child] + (n-subtree[child])
                dfs2(child, node)
                
        dfs2(0, None)
        return res
        
#         # TLE
#         if not edges:
#             return [0]
#         gp = {i:set() for i in range(n)}
#         for i,j in edges:
#             gp[i].add(j)
#             gp[j].add(i)
        
#         check2 = [[0 for _ in range(n)] for _ in range(n)]
#         def get_i_row_col(i):
#             check = [False for _ in range(n)]
#             Q = deque([(i,0)])
#             while Q:
#                 target,dist = Q.popleft()
#                 if check[target]:
#                     continue
#                 check[target] = True
#                 check2[i][target] = dist
#                 check2[target][i] = dist
#                 for j in gp[target]:
#                     if check[j]:
#                         continue
#                     Q.append((j,dist+1))
#             return
        
#         for i in range(n):
#             get_i_row_col(i)
            
#         return [sum(i) for i in check2]