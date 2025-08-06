class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        non_empty = set()
        for fruit in fruits:
            for j in range(len(baskets)):
                if j not in non_empty and fruit <= baskets[j]:
                    n -= 1
                    non_empty.add(j)
                    break
        return n