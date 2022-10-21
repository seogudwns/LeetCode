class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = list(set(strs))
        if len(strs) == 1:
            return strs[0]
        
        base = strs[0]
        leng = len(strs)
        unit = ''
        for i in range(1,len(base)+1):
            unit = base[:i]
            for j in range(1,leng):
                if unit != strs[j][:i]:
                    return base[:i-1]

        return unit