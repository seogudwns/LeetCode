class Solution:
    # def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
#         n, Q, nex, curr = len(heights), [(bricks,ladders)], [], 0
        
#         while curr<n:
#             print(curr,Q)
#             if heights[curr]>=heights[curr+1]:
#                 curr += 1
#                 continue
                
#             if not Q: return curr
#             curr += 1
#             while Q:
#                 x = Q.pop()
#                 if x[0]>=heights[curr+1]-heights[curr]:
#                     nex.append((x[0]-heights[curr+1]+heights[curr],x[1]))
#                 if x[1]>0:
#                     nex.append((x[0],x[1]-1))
            
#             Q,nex = nex,[]
        
#         return n

   def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
       p = []
       
       i = 0
       for i in range(len(h) - 1):
           diff = h[i + 1] - h[i]
           
           if diff <= 0:
               continue
           
           b -= diff
           x = heapq.heappush(p, -diff)
        
           if b < 0:
               b += -heapq.heappop(p)
               l -= 1
               
           if l < 0:
               return i
       return len(h)-1
  
