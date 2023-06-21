class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        i,k = min(nums),max(nums)
        if i==k: return 0
        
        n = len(cost)
        def calc(i): return sum(abs(i-nums[j])*cost[j] for j in range(n))
        
        bef,curr = calc(i),calc(i+1)
        if bef<curr: return bef
        curr,aft = calc(k-1),calc(k)
        if aft<curr: return aft
        
        while i<k:
            mid = (i+k)//2
            bef,curr,aft = calc(mid-1),calc(mid),calc(mid+1)
            if curr<=bef and curr<=aft: return curr
            elif bef<curr:
                k = mid
            else:
                i = mid+1
        
        
#         for i in range(1,max(nums+cost)):
#             print(f'옆의 라인은 {i}로 숫자를 통일할 때 필요한 cost를 보여줍니다. : {sum(abs(i-nums[j])*cost[j] for j in range(len(cost)))}(작을때만 사용하세요.)')
        