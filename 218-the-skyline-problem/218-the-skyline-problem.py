class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        dots = []
        for l,r,h in buildings:
            dots.append([l,-h])
            dots.append([r,h])
            
        dots = sorted(dots)
        
        result = []
        max_heap = [0]
        curr_max_height = 0
        
        for node,height in dots:
            if height<0:
                heapq.heappush(max_heap,height)
            else:
                max_heap.remove(-height)
                heapq.heapify(max_heap)
                
            height_max = -max_heap[0]
            if height_max!=curr_max_height:
                curr_max_height = height_max
                result.append([node,height_max])
                
        return result