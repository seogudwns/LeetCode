class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        s = [i for i in s]
        alp_loc = [i for i in range(len(s)) if s[i].isalpha()]
        for i in alp_loc:
            s[i] = s[i].lower()
        result.append(''.join(s))
        
        for i in range(1,len(alp_loc)+1):
            for j in combinations(alp_loc,i):
                setj = set(j)
                for k in setj:
                    s[k] = s[k].upper()
                result.append(''.join(s))
                for k in setj:
                    s[k] = s[k].lower()
        
        return result
                    