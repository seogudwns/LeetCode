class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return word if not ch in word else word[word.index(ch)::-1]+word[word.index(ch)+1:]