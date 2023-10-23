class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (bin(n).count('1') == 1 and bin(n).count('0')%2) if n>0 else False