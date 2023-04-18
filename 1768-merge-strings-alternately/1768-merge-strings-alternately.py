class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join([(word1[i//2] if len(word1)>i//2 else '') if not i%2 else (word2[i//2] if len(word2)>i//2 else '') for i in range(2*max(len(word1),len(word2)))])