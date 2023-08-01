class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return [list(i) for i in combinations([i for i in range(1,n+1)],k)]
        ans = []
        for i in range(1,1<<n):
            if bin(i).count('1')==k:
                tmp = []
                for j in range(n):
                    if i & 1<<j:
                        tmp.append(j+1)
                ans.append(tmp)
                
        return ans