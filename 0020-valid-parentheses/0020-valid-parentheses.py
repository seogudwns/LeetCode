class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',']':'[','}':'{'}
        op = list(dic.values())
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