class Solution:
    def removeStars(self, s: str) -> str:
        lst=[]
        for i in s: lst.append(i) if i!='*' else lst.pop()
        return ''.join(lst)