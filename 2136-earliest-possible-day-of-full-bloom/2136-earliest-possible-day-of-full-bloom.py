class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        num = -1
        res = 0
        
        for p,g in sorted(zip(plantTime,growTime),key = lambda x:-x[1]):
            num += p
            res = max(res,num+g+1)
        return res