class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        S = []
        x = 0
        
        for i in tokens:
            try:
                tmp = int(i)
                S.append(x)
                x = tmp
            except:
                if i == '+':
                    x += S.pop()
                elif i == '-':
                    x = S.pop()-x
                elif i == '*':
                    x *= S.pop()
                elif i == '/':
                    x = S.pop()//x if x*S[-1]>=0 else - (abs(S.pop())//abs(x))
                    # tmp = S.pop()
                    # if tmp == 0:
                    #     x = 0
                    # elif x*tmp > 0:
                    #     x = tmp//x
                    # else:
                    #     x = - (abs(tmp)//abs(x))
            # print(S,x)
        return x
        
        