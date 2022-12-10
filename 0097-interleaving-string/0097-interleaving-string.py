class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3) or Counter(s1+s2) != Counter(s3):
            return False

        # dp table needs an extra row and col to seperate the base cases 
        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        #initialize dp base cases
        dp[0][0] = True
        for i in range(1,len(s1)+1):
            if s1[i-1] == s3[i-1]:
                dp[i][0] = True
            else:
                break
                
        for j in range(1,len(s2)+1):
            if s2[j-1] == s3[j-1]:
                dp[0][j] = True
            else:
                break
                
        # go through the dp table, for every [row][col], check if previous can be constructed, and check if current 
        # in s1 or s2 is the same as current in s3
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1]):
                    dp[i][j] = True

        return dp[-1][-1]
#         # TLE..
#         if len(s1)+len(s2) != len(s3) or Counter(s1+s2) != Counter(s3):
#             return False
        
#         l,r,lr = len(s1),len(s2),len(s3)
#         Q = [(0,0,0)]
#         while Q:
#             a,b,c = Q.pop()
#             if a == l and b == r:
#                 return True
            
#             if a<l and s1[a] == s3[c]:
#                 Q.append((a+1,b,c+1))
#             if b<r and s2[b] == s3[c]:
#                 Q.append((a,b+1,c+1))
                
#         return False