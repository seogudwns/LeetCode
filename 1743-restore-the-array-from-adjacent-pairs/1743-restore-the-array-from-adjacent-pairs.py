class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        for i,j in adjacentPairs:
            dic[i].append(j)
            dic[j].append(i)
        
        for i in dic:
            if len(dic[i]) == 1:
                break
        
        ans = [i,dic[i][0]]
        bef,curr = i,dic[i][0]
        while len(dic[curr]) != 1:
            for j in dic[curr]:
                if j != bef:
                    ans.append(j)
                    bef,curr = curr,j
                    break
        
        return ans