class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            l,r = 0,len(i)-1
            while True:
                if l>=r:
                    return i
                if i[l] == i[r]:
                    l += 1
                    r -= 1
                else:
                    break
        
        return ""