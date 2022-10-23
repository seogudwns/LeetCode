class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # # using set.
        res = set()
        nums = sorted(nums)
        leng = len(nums)
        for i in range(leng-3):
            for j in range(i+1,leng-2):
                tmp = nums[i]+nums[j]
                k, l = j+1, leng-1
                while k < l:
                    
                    if tmp+nums[k]+nums[l] == target:
                        res.add((nums[i],nums[j],nums[k],nums[l]))
                    if tmp+nums[k]+nums[l] > target:
                        l-=1 
                    else:
                        k+=1 

        return list(res)
    
        # # code with no idea.
        # leng = len(nums)
        # res = []
        # for i in range(leng-3):
        #     for j in range(i+1,leng-2):
        #         tmp = nums[i]+nums[j]
        #         for k in range(j+1,leng-1):
        #             tmp2 = tmp+nums[k]
        #             for w in range(k+1,leng):
        #                 if tmp2+nums[w] == target:
        #                     unit = sorted([nums[i],nums[j],nums[k],nums[w]])
        #                     if unit not in res:
        #                         res.append(unit)
        # return res
        