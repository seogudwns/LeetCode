class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        check = False
        if sum(flowerbed[:2]) == 0:
            cnt = 1
            check = True
        
        for i in range(1,len(flowerbed)):
            if check:
                check = False
                continue
            if sum(flowerbed[i-1:i+2]) == 0:
                cnt += 1
                check = True
        
        return cnt>=n