class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        if candidates[0] > target:
            return []
        
        res = []
        
        Q = deque([[]])
        while Q:
            x = Q.pop()
            curr = sum(x)
            if curr> target:
                continue
            elif curr == target:
                tmp = sorted(x)
                if tmp not in res:
                    res.append(tmp)
                continue
                
            for i in candidates:
                Q.append(x+[i])
        
        return res
# 아니 이게 통과를 한다고??...ㅋㅋㅋㅋㅋㅋㅋㅋ