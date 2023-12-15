class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return (set(paths[i][1] for i in range(len(paths)))-set(paths[i][0] for i in range(len(paths)))).pop()