class Solution:
    def reverseBits(self, n: int) -> int:
        lst = []
        while n:
            lst.append(n%2)
            n//=2
        
        result = 0
        num = 1
        lst = (lst+[0]*(32-len(lst)))[::-1]
        for i in range(32):
            result += lst[i]*num
            num *= 2
        return result
            