# 22.10.18 daily.
class Solution:
    def countAndSay(self, n: int) -> str:
        def change(x):
            lst = []
            tmp = 0
            curr = x[0]
            for i in range(len(x)):
                if curr != x[i]:
                    lst.extend((str(tmp),curr))
                    curr = x[i]
                    tmp = 1
                else:
                    tmp += 1
            lst.extend((str(tmp),curr))
            return ''.join(lst)
        
        num = '1'
        n-=1
        while n:
            num = change(num)
            n -= 1
        
        return num