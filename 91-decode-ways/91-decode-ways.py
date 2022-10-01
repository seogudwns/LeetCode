class Solution:
    def numDecodings(self, s: str) -> int:
#         nums = [str(i+1) for i in range(26)]
        
#         def change_num(arr):
#             if arr.startswith('0'):
#                 return
#             elif not arr:
#                 global result
#                 result += 1
#                 return
#             for i in nums:
#                 if arr.startswith(i):
#                     # print(arr,i)
#                     change_num(arr[len(i):])
        
#         change_num(s)
#         return result
#         # 재귀... Time Limit Exceeded & global result가 재어되지 않음.

        leng = len(s)
        dp = [0 for _ in range(leng+2)]
        dp[leng] = 1
        # print(dp)
        double = [str(i) for i in range(10,27)]
        
        for i in range(len(s)-1,-1,-1):
            sin,dou = 0,0
            if s[i] in '123456789':
                sin += dp[i+1]
            if s[i] == '1' or (i !=leng-1 and s[i] == '2' and s[i+1] in '0123456'):
                dou += dp[i+2]
            dp[i] = sin+dou
        
        # print(dp)
        return dp[0]