class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        b,c = 0,s.count('0')
        # idx 기준으로 이후에 오른쪽에 1이 몇개있는지 & 왼쪽에 0이 몇개있는지 count.
        
        res = {c}
        for i in range(len(s)):
            if s[i] == '0':
                c-=1
            else:
                b+=1
            res.add(b+c)
        
        # print(res)
        return min(res)