class Solution:
    def oddString(self, words: List[str]) -> str:
        base = min(ord(i) for i in words[0])
        comp = defaultdict(list)
        for i in words:
            base2 = ord(i[0])-base
            comp[''.join(chr(ord(j)-base2) for j in i)].append(i)
        
        for i in comp:
            if len(comp[i]) == 1:
                return comp[i][0]
            
        
        