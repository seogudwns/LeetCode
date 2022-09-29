from collections import Counter

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        
        def cnt_num(num):
            left = 0
            cnt = 0
    
            for i in range(len(nums)):
                while nums[i] - nums[left]>num:
                    left += 1
                    
                cnt += i-left
            
            return cnt
        
        left,right = 0, nums[-1]-nums[0]

        while left<right:
            # print(left,right)
            mid = (left+right)//2
            res = cnt_num(mid)
            
            if res >= k:
                right = mid
            else:
                left = mid+1
                
        return left
    
#         # fail the last test 
#         cnt2 = Counter(nums)
#         dist_nums = sorted(cnt2)
#         n = len(dist_nums)
#         cnt = {abs(i-j):0 for i in dist_nums for j in dist_nums}
#         # print(cnt2)
#         for i in range(n):
#             tmp1 = cnt2[dist_nums[i]]
#             cnt[0] += (tmp1*(tmp1-1))//2
#             for j in range(i+1,n):
#                 cnt[abs(dist_nums[i]-dist_nums[j])] += tmp1*cnt2[dist_nums[j]]
        
#         print(cnt2)
#         print(cnt)
        
#         dif = sorted(cnt)
#         for i in dif:
#             if cnt[i]<k:
#                 k-=cnt[i]
#             else:
#                 return i
        