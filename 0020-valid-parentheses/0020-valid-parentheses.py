class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',']':'[','}':'{'}
        op,cl = list(dic.values()),list(dic.keys())
        lst = []
        for i in s:
            if i in op:
                lst.append(i)
            else:
                if not len(lst) or lst[-1] != dic[i]:
                    return False
                lst.pop()                
        
        if not len(lst):
            return True

        return False