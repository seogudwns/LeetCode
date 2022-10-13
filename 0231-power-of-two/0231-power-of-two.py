class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if bin(n).count('1') != 1 or n <= 0:
            return False
        
        return True