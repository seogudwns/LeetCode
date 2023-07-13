class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        gp = [[] for _ in range(numCourses)]
        chkset = [False for _ in range(numCourses)]
        
        for i,j in prerequisites:
            gp[i].append(j)
        
        @lru_cache(None)
        def dfs(curr):
            if chkset[curr]:
                return False
            
            chkset[curr] = True
            for i in gp[curr]: 
                if not dfs(i): return False
            chkset[curr] = False
                
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True