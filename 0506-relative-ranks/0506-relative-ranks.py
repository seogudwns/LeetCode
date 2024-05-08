class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        tmp = sorted(score,reverse=True)
        tmp2 = {tmp[i]:str(i+1) for i in range(len(score))}
        tmp2[tmp[0]] = "Gold Medal"
        if len(tmp)>1: tmp2[tmp[1]] = "Silver Medal"
        if len(tmp)>2: tmp2[tmp[2]] = "Bronze Medal"
        return [tmp2[score[i]] for i in range(len(score))]