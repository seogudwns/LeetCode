class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        SA,dp = sorted(zip(scores,ages)),[0 for _ in range(max(ages)+1)]
        for score,age in SA: dp[age] = score+max(dp[:age+1])
        return max(dp)