class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        
        bigp = [-1 for _ in range(n+1)]
        bigp[dislikes[0][0]] = 0
        dislikes = deque(dislikes)
        tmp = deque()
        while True:
            while dislikes:
                x,y = dislikes.popleft()
                
                if bigp[x] != -1 and bigp[y] != -1:
                    if bigp[x]%2 == bigp[y]%2:
                        return False
                elif bigp[x] != -1:
                    bigp[y] = bigp[x] + 1
                elif bigp[y] != -1:
                    bigp[x] = bigp[y] + 1
                else:
                    tmp.append((x,y))
                    
            if not tmp:
                print(bigp)
                return True
            if bigp[tmp[0][0]] == -1:
                bigp[tmp[0][0]] = 0
            dislikes = tmp
            tmp = deque()