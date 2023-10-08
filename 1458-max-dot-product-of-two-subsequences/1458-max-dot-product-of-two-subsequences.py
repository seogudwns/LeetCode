class Solution:
    @lru_cache(None)
    def dp(self,i, j):
        if i == self.n or j == self.m:
            return self.mini

        if self.memo[i][j] != self.mini:
            return self.memo[i][j]

        self.memo[i][j] = max(
            self.nums1[i] * self.nums2[j] + max(self.dp(i + 1, j + 1), 0),
            self.dp(i + 1, j),  
            self.dp(i, j + 1), 
        )

        return self.memo[i][j]
    
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        self.nums1,self.nums2 = nums1,nums2
        self.n,self. m,self.mini = len(nums1), len(nums2),-10000001
        self.memo = [[self.mini] * self.m for _ in range(self.n)]
        
        return self.dp(0,0)