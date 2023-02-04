class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1),len(s2)
        if n1 > n2:
            return False
        X = Counter(s1)
        Y = Counter(s2[:n1-1])
        for i in range(n1-1,n2):
            Y[s2[i]] += 1
            # print(X,Y)
            if X == Y: return True
            Y[s2[i+1-n1]] -= 1
        return False

# 예전꺼.
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         char_lst = [0 for _ in range(26)]
#         for i in s1:
#             char_lst[ord(i)-97] += 1
        
#         leng = len(s1)
#         comp_lst = [0 for _ in range(26)]
#         for i in s2[:leng]:
#             comp_lst[ord(i)-97] += 1
            
#         if comp_lst == char_lst:
#             return True
        
#         for i in range(leng,len(s2)):
#             comp_lst[ord(s2[i-leng])-97] -= 1
#             comp_lst[ord(s2[i])-97] += 1
#             if comp_lst == char_lst:
#                 return True
        
#         return False