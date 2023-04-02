class Solution:
    def successfulPairs(self, spells, potions, success):
        potions = sorted(potions)
        result = []
        for a in spells:
            count = len(potions) - bisect_left(potions, (success + a - 1) // a)
            result.append(count)
        return result