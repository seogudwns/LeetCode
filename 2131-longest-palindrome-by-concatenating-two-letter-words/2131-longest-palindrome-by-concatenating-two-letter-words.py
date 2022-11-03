# 22.11.03 daily
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter()

        res = 0
        while words:
            word = words.pop()
            rvs = word[::-1]
            
            if counter[rvs] > 0:
                res += 1
                counter[rvs] -= 1
            else:
                counter[word] += 1
        
        res = 2*(2*res+any(word[0] == word[1] for word in counter if counter[word]>0))
        # del counter
        return res
