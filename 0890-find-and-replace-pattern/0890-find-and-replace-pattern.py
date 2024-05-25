class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans,n = [],len(pattern)
        
        while words:
            i = words.pop()
            chk = True
            tmp1,tmp2 = dict(),dict()
            for j in range(n):
                if pattern[j] not in tmp1:
                    if i[j] not in tmp2:
                        tmp1[pattern[j]] = i[j]
                        tmp2[i[j]] = pattern[j]
                    else:
                        chk = False
                        break
                elif tmp1[pattern[j]] != i[j] or i[j] not in tmp2 or tmp2[i[j]] != pattern[j]:
                    chk = False
                    break
                    
            if chk: ans.append(i)
            
        return ans