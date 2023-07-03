# class Solution:
#     def buddyStrings(self, s: str, goal: str) -> bool:
#         if len(s)!= len(goal): return False
#         n = len(s)
#         x,y = [],[]
#         for i in range(n):
#             if goal[i] != s[i]:
#                 x.append(goal[i])
#                 y.append(s[i])
#         print(x,y)
#         return (len(x)==2 and x[::-1]==y)

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
            
        dif = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                dif.append(i)
        

        if len(dif) != 2:
            if len(dif) == 0 and max(Counter(s).values())>1:
                return True
            return False
        
        if (s[dif[1]] != goal[dif[0]] or s[dif[0]] != goal[dif[1]]):
            return False
        
        return True