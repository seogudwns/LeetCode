class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        aim = len(graph)-1
        
        res = []
        Q = deque([[0]])
        while Q:
            path = Q.popleft()
            for i in graph[path[-1]]:
                if i == aim:
                    res.append(path+[aim])
                else:
                    Q.append(path+[i])
        
        return res