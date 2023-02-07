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
        
        if len(cnts) == 1: return cnts[0][1]
        ans,cnt,basket = cnts[0][1]+cnts[1][1],cnts[0][1],{cnts[0][0],cnts[1][0]}
        for i in range(1,len(cnts)):
            bef = cnts[i][1]
            if cnts[i][0] in basket: cnt += bef
            else: ans,cnt,basket = max(ans,cnt),bef+cnts[i-1][1],{cnts[i-1][0],cnts[i][0]}
        
        return max(ans,cnt)