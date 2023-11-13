class Solution:
    def sortVowels(self, s: str) -> str:
        s,candid,idx,vowels = [i for i in s],[],[],['a','e','i','o','u','A','E','I','O','U']
        for i in range(len(s)):
            if s[i] in vowels:
                idx.append(i)
                heapq.heappush(candid,s[i])
                
        curr = 0
        while candid:
            s[idx[curr]] = heapq.heappop(candid)
            curr += 1

        return ''.join(s)
        