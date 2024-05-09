class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness)
        ans = 0
        for i in range(k):
            ans = max(ans,ans+happiness.pop()-i)
        return ans