class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        x = 0
        while x < len(s):
            if s[x] == '#':
                if x == 0:
                    s = s[1:]
                else:
                    s = s[:x-1]+s[x+1:]
                    x-=1
            else:
                x+=1
        x = 0
        while x < len(t):
            if t[x] == '#':
                if x == 0:
                    t = t[1:]
                else:
                    t = t[:x-1]+t[x+1:]
                    x-=1
            else:
                x+=1
        
        return s==t