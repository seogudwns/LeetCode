class Solution:
    def Qs(self,lst):
        if len(lst)<2: return lst

        curr,sm,la = lst.pop(),[],[]
        for i in lst:
            if i<=curr: sm.append(i)
            else: la.append(i)

        return self.Qs(sm)+[curr]+self.Qs(la)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        # return self.Qs(nums)
        return sorted(nums)