class Solution:
    def tribonacci(self, n: int) -> int:
        A,X = 2**32,[0,1,1]
        if n<3: return X[n]
        for i in range(n-2): X.append(sum(X[-3:])%A)
        return X[-1]