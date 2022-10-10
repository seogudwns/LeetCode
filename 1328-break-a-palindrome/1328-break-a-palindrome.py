class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        leng = len(palindrome)
        for i in range(leng+1):
            try:
                if palindrome[i] !='a':
                    if i == leng//2 and leng%2:
                        continue
                    break
            except:
                break
        
        if i != leng:
            return palindrome[:i]+'a'+palindrome[i+1:]
        else:
            return palindrome[:-1]+'b'