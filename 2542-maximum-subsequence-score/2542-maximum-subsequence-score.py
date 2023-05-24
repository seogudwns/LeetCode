class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        x = sorted(zip(nums1,nums2),key=lambda y:(-y[1],y[0]))
        n1sum,n1heapq = 0,[]
        
        for i in range(k):
            n1sum+=x[i][0]
            heapq.heappush(n1heapq,x[i][0])
            
        ans = n1sum*x[k-1][1]
        
        for i in range(k,len(nums1)):
            if x[i][0]>n1heapq[0]:
                n1sum += x[i][0]-heapq.heappop(n1heapq)
                heapq.heappush(n1heapq,x[i][0])
            ans = max(ans,x[i][1]*n1sum)
        
        return ans