class Solution:
    def myAtoi(self, s: str) -> int:
        # "-91283472332" --> -2147483648 .... ????
        leng = len(s)
        i = -1
        while True:
            try:
                i += 1
                if s[i] == ' ':
                    continue
                elif s[i] in '1234567890+-':
                    break
                else:
                    return 0
            except:
                return 0 
                # s contains no '1234567890+-'.
                
        # s[i] in '1234567890+-', before i, there is no string_number.        

        lst = []
        if s[i] in '+-':
            if i == leng-1 or s[i+1] not in '1234567890':
                return 0
        
            if s[i] == '-':
                lst.append(s[i])
                i += 1
            elif s[i] == '+':
                i += 1
                
        while i != leng:
            if s[i] not in '1234567890':
                break
            lst.append(s[i])
            i+=1
        result = int(''.join(lst))
        if -2**31<=result<=2**31-1:
            return result
        else:
            if result<0:
                return -(2**31)
            return (2**31)-1