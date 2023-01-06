class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs,reverse=True)
        res = 0
        while costs:
            if costs[-1]>coins:
                break
            coins -= costs.pop()
            res += 1
        
        return res