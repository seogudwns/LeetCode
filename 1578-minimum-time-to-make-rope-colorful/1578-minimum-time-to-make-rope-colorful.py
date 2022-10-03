class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        leng = len(colors)
        conse_lst = []
        curr = colors[0]
        tmp = []
        for i in range(leng):
            if colors[i] != curr:
                curr = colors[i]
                conse_lst.append(tmp)
                tmp = [i]
            else:
                tmp.append(i)
        
        if tmp:
            conse_lst.append(tmp)
        
        result = 0
        for i in conse_lst:
            if len(i) == 1:
                continue
                
            maxi = 0
            subt = 0
            for j in i:
                subt += neededTime[j]
                if neededTime[j]>maxi:
                    maxi = neededTime[j]
            
            result += subt-maxi
            
        return result
    # 합치면 더 효율이 좋기는 하지만 귀찮다.