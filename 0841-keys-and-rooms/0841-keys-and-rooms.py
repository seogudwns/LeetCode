class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        check = [False for _ in rooms]
        check[0] = True
        Q = deque(rooms[0])
        while Q:
            x = Q.popleft()
            
            if check[x]:
                continue
            check[x] = True
            
            for i in rooms[x]:
                if check[i]:
                    continue
                Q.append(i)
        
        for i in check:
            if not i:
                return False
        return True