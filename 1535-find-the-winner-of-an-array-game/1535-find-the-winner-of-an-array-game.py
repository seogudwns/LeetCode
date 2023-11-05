class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        CC = Counter()
        arr = deque(arr)
        cnt = 0
        arrmax = max(arr)
        while cnt<k:
            x,y = arr.popleft(),arr.popleft()
            if x == arrmax: return x
            if x<y: 
                x,y = y,x
                cnt = 0
                
            CC[x]+=1
            arr.appendleft(x)
            arr.append(y)
            cnt += 1
        
        return {i for i in CC if CC[i] == max(CC.values())}.pop()