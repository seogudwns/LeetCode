class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]]+[pref[i]^pref[i+1] for i in range(len(pref)-1)]