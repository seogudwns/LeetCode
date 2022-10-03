class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
#         leng = len(colors)
#         conse_lst = []
#         curr = colors[0]
#         tmp = []
#         for i in range(leng):
#             if colors[i] != curr:
#                 curr = colors[i]
#                 conse_lst.append(tmp)
#                 tmp = [i]
#             else:
#                 tmp.append(i)
        
#         if tmp:
#             conse_lst.append(tmp)
        
#         result = 0
#         for i in conse_lst:
#             if len(i) == 1:
#                 continue
                
#             maxi = 0
#             subt = 0
#             for j in i:
#                 subt += neededTime[j]
#                 if neededTime[j]>maxi:
#                     maxi = neededTime[j]
            
#             result += subt-maxi
            
#         return result
    # 합치면 더 효율이 좋기는 하지만 귀찮다.. 합치자.. 효율 개똥망이네.
#         def calc_remind_maxi(lst):
#             if len(lst) == 1:
#                 return 0
            
#             subt = 0
#             maxi = 0
#             for j in lst:
#                 subt += neededTime[j]
#                 if neededTime[j]>maxi:
#                     maxi = neededTime[j]
#             return subt-maxi
        
#         leng = len(colors)
#         curr = colors[0]
#         tmp = [0]
#         result = 0
        
#         for i in range(1,leng):
#             if colors[i] != curr:
#                 curr = colors[i]
#                 result += calc_remind_maxi(tmp)
#                 tmp = [i]
                
#             else:
#                 tmp.append(i)
        
#         if len(tmp)>1:
#             result += calc_remind_maxi(tmp)
            
#         return result
#         # 좀 더 개선해보자.
        
        leng = len(colors)
        curr = colors[0]
        start = 0
        result = 0
        
        for i in range(1,leng):
            if colors[i] != curr:
                curr = colors[i]
                result += sum(neededTime[start:i])-max(neededTime[start:i])
                start = i
        
        if start != i:
            result += sum(neededTime[start:leng])-max(neededTime[start:leng])
        
        return result