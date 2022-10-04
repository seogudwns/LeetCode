class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split()
        for i in range(len(s_split)):
            s_split[i] = s_split[i][::-1]
        
        return ' '.join(s_split)