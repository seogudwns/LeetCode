class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        player = [[10**9 for _ in range(n)] for _ in range(n)]

        def game(l, r):
            if l == r: player[l][r] = nums[l]
            elif player[l][r] == 10**9: player[l][r]=max(nums[l]-game(l+1,r), nums[r]-game(l, r-1))
            return player[l][r]
        
        return game(0, n - 1) >= 0