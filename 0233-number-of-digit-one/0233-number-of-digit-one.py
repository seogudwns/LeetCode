class Solution:
    def countDigitOne(self, n: int) -> int:
        
        strn = str(n)
        leng = len(strn)
        if leng == 1:
            if n == 0:
                return 0
            else:
                return 1
            
        res = 0
        # 가장 큰 자리수에 대한 계산.
        if strn[0] == '1':
            res += int(strn[1:])+1
        else:
            res += 10**(leng-1)
        # print(res)
        
        # 1의 자리에 대한 계산.
        if strn[-1] == '0':
            res += int(strn[:-1])
        else:
            res += int(strn[:-1])+1
        # print(res)
        
        # 나머지 자리에 대한 계산.
        for i in range(1,leng-1):
            if strn[i] == '0':
                res += int(strn[:i])*10**(leng-1-i)
            elif strn[i] == '1':
                res += int(strn[:i])*10**(leng-1-i)+int(strn[i+1:])+1        
            else:
                res += (int(strn[:i])+1)*10**(leng-1-i)
        
        return res