class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors)<3: return False
        a,b = 0,0
        curr = 0
        for i in range(3): curr +=1 if colors[i] == 'A' else -1
        
        if curr == 3: a += 1
        elif curr == -3: b += 1

        for i in range(3,len(colors)):
            curr += 1 if colors[i] == 'A' else -1
            curr -= 1 if colors[i-3] == 'A' else -1
            if curr == 3: a += 1
            elif curr == -3: b += 1

        return a>b
        
        