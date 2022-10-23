class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        leng = len(digits)
        changer = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        curr = ['']
        nex = []
        l = 0
        while l != leng:
            for i in curr:
                for j in changer[digits[l]]:
                    nex.append(i+j)
            
            curr = nex
            nex = []
            l += 1
        
        return curr