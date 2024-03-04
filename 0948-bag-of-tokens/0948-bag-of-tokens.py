class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        curr_score = 0
        tokens = sorted(tokens)
        l,r = 0,len(tokens)-1
        
        while l<=r:
            if power-tokens[l]>=0:
                curr_score += 1
                power -= tokens[l]
                l += 1
                score = max(score,curr_score)
            elif score > 0:
                curr_score -= 1
                power += tokens[r]
                r -= 1
            else:
                break
        
        return score
