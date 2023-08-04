class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lens = len(s)
        
        @lru_cache(None)
        def chk(leng:int):
            if not leng: return True
            elif leng<0: return False
            return any(chk(leng-len(i)) if s[:leng].endswith(i) else False for i in wordDict)
        
        return chk(lens)
                