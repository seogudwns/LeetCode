class Solution:
    
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        rem = [0 for _ in range(26)]
        for i in letters: rem[ord(i)-97] += 1
        fails = set()
        ans = 0
        for i in range(1<<len(words)):
            for j in fails:
                if i&j == j:
                    break
            else:
                tmp = [0 for _ in range(26)]
                for j in range(len(words)):
                    if 2**j & i:
                        for k in words[j]:
                            tmp[ord(k)-97]+=1
                
                if all(rem[j]-tmp[j]>=0 for j in range(26)):
                    ans = max(ans,sum(tmp[i]*score[i] for i in range(26)))
                else:
                    fails.add(i)
                    
        return ans