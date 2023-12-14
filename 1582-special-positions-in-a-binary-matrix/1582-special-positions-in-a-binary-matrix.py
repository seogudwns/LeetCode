class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        candid = set()
        for i in range(len(mat)):
            if sum(mat[i])==1: 
                for j in range(len(mat[0])):
                    if mat[i][j] == 1:
                        candid.add(j)
                        break
                        
        ans = 0
        while candid:
            x = candid.pop()
            if sum(mat[i][x] for i in range(len(mat))) == 1:
                ans+=1
        
        return ans