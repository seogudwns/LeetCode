class Solution:
    def numSteps(self, s: str) -> int:
        if s == '1': return 0
        ans = 0
        s =[i for i in s]
        while len(s) != 1:
            x = s.pop()
            if x == '2': 
                s[-1] = str(int(s[-1])+1)
                ans +=1
            elif x == '1': 
                s[-1] = str(int(s[-1])+1)
                ans += 2
            else:
                ans += 1
                
                
        return ans+1 if s[0] == '2' else ans        