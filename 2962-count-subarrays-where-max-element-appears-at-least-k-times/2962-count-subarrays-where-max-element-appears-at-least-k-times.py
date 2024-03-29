class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l,maxi,n,cnt,ans = 0,max(nums),len(nums),0,0

        for i in range(n):
            if nums[i]==maxi: cnt+=1
            while cnt>=k:
                if nums[l]==maxi: cnt-=1
                l+=1
            ans+=l
            
        return ans