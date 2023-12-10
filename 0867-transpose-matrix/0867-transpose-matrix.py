class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [i for i in zip(*[i for i in matrix])]