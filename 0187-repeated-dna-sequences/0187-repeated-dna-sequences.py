class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        x = Counter(s[i:i+10] for i in range(len(s)-9))
        return [i for i in x if x[i]>1]