class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= ''.join(re.findall('[a-z|A-Z|0-9]',s)).lower()
        if not s:
            return True
        # print(s,len(s))
        for i in range(len(s)//2+1):
            if s[i] != s[-1-i]:
                return False
        return True