class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        curr = 0
        nex = 1
        for i in columnTitle[::-1]:
            curr += (ord(i)-64)*nex
            nex *= 26
        
        return curr