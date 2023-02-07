class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits)<3: return len(fruits)
        
        cnts,cnt,curr = [],0,fruits[0]
        for i in range(len(fruits)):
            if curr == fruits[i]: cnt+=1
            else:
                cnts.append((curr,cnt))
                curr,cnt = fruits[i],1
        cnts.append((curr,cnt))
        # print(cnts)
        if len(cnts) == 1: return cnts[0][1]
        ans,cnt,basket = cnts[0][1]+cnts[1][1],cnts[0][1],{cnts[0][0],cnts[1][0]}
        for i in range(1,len(cnts)):
            bef = cnts[i][1]
            if cnts[i][0] in basket: cnt += bef
            else: ans,cnt,basket = max(ans,cnt),bef+cnts[i-1][1],{cnts[i-1][0],cnts[i][0]}
            # print(i,ans,cnt,basket)
        
        return max(ans,cnt)
        
#         curr,start,bef,ans = fruits[:2],-1,0,2
#         for i in range(2,len(fruits)):
#             if fruits[i] in curr:
#                 if fruits[i] == curr[0]: curr[:],bef = curr[::-1],i-1
#             else: ans,start,bef,curr = max(ans,i-start),bef,i-1,[fruits[i-1],fruits[i]]
#             print(ans,i,curr,start,bef)
        
#         return max(ans,i-start)
    
#     [3,3,3,1,2,1,1,2,3,3,4]
#     [3,3,3,3,1,1,1,1,1]
#     [3,3,3,3,1,1,1,1,1,3,4]