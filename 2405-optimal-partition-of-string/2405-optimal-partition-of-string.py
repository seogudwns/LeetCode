class Solution:
    def partitionString(self, s: str) -> int:
        tmp,ans = set(),1
        for i in s:
            if i in tmp:
                tmp = {i}
                ans+=1
            else:
                tmp.add(i)
        return ans