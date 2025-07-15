class Solution:
    def isValid(self, word: str) -> bool:
        return len(word)>2 and word.isalnum() and any(i for i in word.lower() if i.isalpha() and i in 'aeiou') and any(i for i in word.lower() if i.isalpha() and i not in 'aeiou')
