class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        leng = len(x)
        # print(x[:leng//2],x[leng-1:(leng-1)//2:-1])
        if x[:leng//2] != x[leng-1:(leng-1)//2:-1]:
            return False
        
        return True