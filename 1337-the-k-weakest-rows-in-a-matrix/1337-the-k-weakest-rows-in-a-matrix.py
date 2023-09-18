class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i for i,j in sorted(enumerate(mat),key=lambda x: sum(x[1]))][:k]