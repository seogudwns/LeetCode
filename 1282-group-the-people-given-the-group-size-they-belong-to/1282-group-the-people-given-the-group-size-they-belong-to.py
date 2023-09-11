class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        tmp = sorted(enumerate(groupSizes),key = lambda x:(x[1],x[0]),reverse=True)
        ans = []
        while tmp:
            s = tmp[-1][1]
            curr = []
            for i in range(s):
                x,y = tmp.pop()
                curr.append(x)
            ans.append(curr)
        return ans