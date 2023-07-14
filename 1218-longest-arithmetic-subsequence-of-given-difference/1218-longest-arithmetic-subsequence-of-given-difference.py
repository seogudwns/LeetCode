class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if difference==0: return max(Counter(arr).values())
        X = dict()
        for i in arr:
            if i-difference in X:
                X[i] = X[i-difference]+1
                del X[i-difference]
            elif i in X: continue
            else: X[i] = 1
                
        return max(X.values())