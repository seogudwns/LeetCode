class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        if n <= 2:
            return 1
    
#         half = n//2+1
#         start = 1
#         end = 2
#         result = 1
#         num = 3
#         while True:
#             # print(start,end,num)
#             if end<half:
#                 if num < n:
#                     end += 1
#                     num += end
#                 elif num == n:
#                     result += 1
#                     num -= start
#                     start += 1
#                 elif num > n:
#                     num -= start
#                     start += 1
#             else: # end == half:
#                 if num > n:
#                     num -= start
#                     start += 1
#                 elif num == n:
#                     result += 1
#                     return result
#                 else:
#                     return result
#                 투 포인터로는 시간초과..

        while n%2==0:
            n //= 2
        result = 1
        p = 3
        tmp = 1
        while n != 1:
            tmp = 1
            while n%p==0:
                tmp+=1
                n //= p
            result *= tmp
            
            if p**2>=n:
                if n>=p:
                    result *= 2
                break
                
            p += 2
            
        return result
    # from https://leetcode.com/problems/consecutive-numbers-sum/discuss/2468063/Very-simple-Python-solution-beats-most-submissions-oror-Very-simple