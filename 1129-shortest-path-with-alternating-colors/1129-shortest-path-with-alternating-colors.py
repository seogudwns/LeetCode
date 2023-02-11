class Solution:
    def shortestAlternatingPaths(self, numOfNodes: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph,maxSize = [[[], []] for i in range(numOfNodes)],10**5+1
        for start, end in redEdges: graph[start][0].append(end)
        for start, end in blueEdges: graph[start][1].append(end)
            
        distances = [[0, 0]] + [[maxSize,maxSize] for i in range(numOfNodes - 1)]
        queue = [[0, 0], [0, 1]]
        for node, color in queue:
            for neighbor in graph[node][color]:
                if distances[neighbor][color] == maxSize:
                    distances[neighbor][color] = distances[node][1 - color] + 1
                    queue.append([neighbor, 1 - color])
        return [dist if dist < maxSize else -1 for dist in map(min, distances)]