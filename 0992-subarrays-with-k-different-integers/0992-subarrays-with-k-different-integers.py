class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        
        def solve(k: int) -> int:
            nonlocal nums
            ans = 0
            n = len(nums)
            cnt = defaultdict(int)
            diff = 0

            l = 0
            for r in range(n):
                cnt[nums[r]] += 1
                if cnt[nums[r]] == 1:
                    diff += 1
                while diff > k:
                    cnt[nums[l]] -= 1
                    if cnt[nums[l]] == 0:
                        diff -= 1
                    l += 1
                    
                # print(l,r)
                ans += (r - l + 1)
            # print(ans)
            return ans
        
        return solve(k) - solve(k - 1)
        