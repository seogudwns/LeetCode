# n == 3
# [000, 001, 011, 010, 110, 111, 101, 100]
# n == 4
# [0000, 0001, 0011, 0010, 0110, 0111, 0101, 0100, 1100, 1101, 1111, 1110, 1010, 1011, 1001, 1000]

class Solution:
    def grayCode(self, n: int) -> List[int]:
        init = [0,1]
        mul = 1
        for _ in range(n-1):
            mul *= 2
            init = [i for i in init] + [mul+i for i in init[::-1]]
            
        return init