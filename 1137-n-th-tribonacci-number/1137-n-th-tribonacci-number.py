class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        elif n < 3: return 1
        A,X = 2**32,[0,1,1]
        for i in range(n-2): X.append(sum(X[-3:])%A)
        return X[-1]