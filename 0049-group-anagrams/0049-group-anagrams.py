# 22.10.28 Daily 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for i in strs:
            x = ''.join(sorted(i))
            if x not in dic:
                dic[x] = []
            dic[x].append(i)
        
        return list(dic.values())