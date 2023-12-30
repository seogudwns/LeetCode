class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt,cnter = len(words),Counter()
        for i in words:
            for j in i:
                cnter[j]+=1
        
        return all(cnter[x]%cnt == 0 for x in cnter)