class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def chk(i,j):
            if j-i==1: return True
            tmp = sorted(nums[i:j+1])
            comp = tmp[1]-tmp[0]
            return all(tmp[k+1]-tmp[k] == comp for k in range(j-i))
        
        return [chk(l[i],r[i]) for i in range(len(l))]