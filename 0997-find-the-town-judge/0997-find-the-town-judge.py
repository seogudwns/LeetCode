class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        X = defaultdict(int)
        for i,j in trust:
            X[i]+=1
            X[j]-=1
        if list(X.values()).count(-n+1)==1:
            for i in X:
                if X[i] == -n+1:
                    return i
        return -1