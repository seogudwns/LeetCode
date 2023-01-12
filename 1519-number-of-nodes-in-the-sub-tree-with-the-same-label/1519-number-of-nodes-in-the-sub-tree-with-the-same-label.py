class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        g, labelCt, ans, labels = defaultdict(set), [0]*26, [0]*n, [ord(i)-97 for i in labels]
        
        for a, b in edges: 
            g[a].add(b)
            g[b].add(a)
        
        def dfs(node=0, par=None):
            prev = labelCt[labels[node]]
            labelCt[labels[node]] += 1
            
            for child in g[node]:
                if child != par: dfs(child, node)

            ans[node] = labelCt[labels[node]] - prev

        dfs()
        return ans