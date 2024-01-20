class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        stack = []
        n = len(arr)
        arr.append(0)
        for i, num in enumerate(arr):
            while stack and (i == n or num < arr[stack[-1]]):
                top = stack.pop()
                starts = top - stack[-1] if stack else top + 1
                ends = i - top
                res += (starts * ends * arr[top])%MOD
                
            stack.append(i)
        
        return res%MOD