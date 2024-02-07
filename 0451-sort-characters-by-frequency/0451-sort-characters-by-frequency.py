class Solution:
    def frequencySort(self, s: str) -> str:
        cnter = Counter(s)
        return ''.join(i*cnter[i] for i in sorted(cnter,key=lambda x: -cnter[x]))