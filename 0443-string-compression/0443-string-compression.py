# class Solution:
#     def compress(self, chars: List[str]) -> List:
#         char,cnt,ans = chars[0],0,[]
        
#         for i in chars:
#             if char == i: cnt += 1
#             else:
#                 ans.append(char)
#                 char = i
#                 if cnt != 1: ans.extend(j for j in str(cnt))
#                 cnt = 1
                
#         ans.append(char)
#         if cnt != 1: ans.extend(j for j in str(cnt))
        
#         print(ans)
#         return ans
    
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1: return 1
        
        i,j = 0,0
        
        while i < n:
            count = 1
            while i < n - 1 and chars[i] == chars[i+1]:
                count += 1
                i += 1
            
            chars[j] = chars[i]
            j += 1
            
            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1
            
            i += 1
        
        return j