class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordern = {order[i]:i for i in range(26)}
        # print(ordern)
        bef,aft = '',words[0]
        for i in range(1,len(words)):
            bef,aft = aft,words[i]
            if aft==bef:
                continue
            elif aft.startswith(bef) and len(aft)>len(bef):
                continue
            elif bef.startswith(aft) and len(bef)>len(aft):
                return False
            for j in range(min(len(bef),len(aft))):
                if ordern[bef[j]]<ordern[aft[j]]:
                    break
                elif ordern[bef[j]]>ordern[aft[j]]:
                    return False
                    
        return True