class Solution:
    def numSquares(self, n: int) -> int:
        res = [i for i in range(n+1)]
        perf = [1]
        for i in range(2,n+1):
            if (i**0.5).is_integer():
                res[i] = 1
                perf.append(i)
            else:
                for j in perf:
                    res[i] = min(res[i],res[i-j]+1)

        return res[-1]