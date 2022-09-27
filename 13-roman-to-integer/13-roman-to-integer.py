class Solution:
    def romanToInt(self, s: str) -> int:
        div_dict = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        div_dict2 = {'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4}
        num = 0
        for i in div_dict2:
            if i in s:
                num += div_dict2[i]
                s = s.replace(i,'')
                
        for i in s:
            num += div_dict[i]
        return num