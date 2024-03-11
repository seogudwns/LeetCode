class Solution:
    def customSortString(self, order: str, s: str) -> str:
        x = Counter(s)
        ans = []
        for i in order:
            if i in x:
                ans.append(i*x[i])
                del x[i]
        
        return ''.join(ans+[x[i]*i for i in sorted(x)])