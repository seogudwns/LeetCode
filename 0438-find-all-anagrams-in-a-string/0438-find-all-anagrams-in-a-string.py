class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1,n2 = len(s),len(p)
        if n1<n2:
            return []
        
        ans,X,Y = [],[0]*26,[0]*26
        
        for i in p: X[ord(i)-97] += 1
        for i in s[:n2-1]: Y[ord(i)-97] += 1
            
        for i in range(n1-n2+1):
            Y[ord(s[i+n2-1])-97]+=1
            if X==Y: ans.append(i)
            Y[ord(s[i])-97]-=1
            
        return ans
        