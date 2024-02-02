class Solution:
    def __init__(self):
        self.ans = []
        
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def inputnums(n,cnt=0):
            if low<=n<=high: self.ans.append(n)
            if cnt == 10: return;
            if n%10 != 9: inputnums(n*10+n%10+1,cnt+1)
            
        for i in range(1,10):
            inputnums(i)
        
        return sorted(self.ans)