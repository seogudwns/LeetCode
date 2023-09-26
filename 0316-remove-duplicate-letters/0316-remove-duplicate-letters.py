class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n=len(s)
        lookup={}
        for i in range(n):
            lookup[s[i]]=i
        ans=[]
        for i in range(n):
            if s[i] not in ans:
                while ans and ans[-1]>s[i] and lookup[ans[-1]]>i:
                    ans.pop()
                ans.append(s[i])
        return "".join(ans)