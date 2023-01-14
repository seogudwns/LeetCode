class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        lst = [i for i in range(ord('z')+1)] # ord('a') == 97, ord('z') == 121
        def find(x):
            if x != lst[x]:
                lst[x] = find(lst[x])
            return lst[x]
            
        def union(x,y):
            x = find(x)
            y = find(y)
            if x != y:
                lst[x] = lst[y] = min(x,y)
        
        for i in range(len(s1)):
            union(ord(s1[i]),ord(s2[i]))
        for x in range(97,122):
            lst[x] = find(x)
            
        return ''.join([chr(lst[ord(i)]) for i in baseStr])