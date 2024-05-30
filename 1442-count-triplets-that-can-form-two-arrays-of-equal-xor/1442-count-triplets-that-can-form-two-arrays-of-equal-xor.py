class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n,ans = len(arr),0
        for i in range(n):
            chk = arr[i]
            for j in range(i+1,n):
                chk ^= arr[j]
                if chk == 0:
                    ans += j-i
        
        return ans