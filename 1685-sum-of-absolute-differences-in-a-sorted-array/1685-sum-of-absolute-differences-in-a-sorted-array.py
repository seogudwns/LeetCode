class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s,s1,pref,suff = 0,sum(nums),[],[]

        for num in nums:
            s += num
            pref.append(s)
            suff.append(s1)
            s1 -= num
        return [suff[i]+nums[i]*(2*i+1-len(nums)) - pref[i] for i in range(len(nums))]