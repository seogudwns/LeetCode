class UndergroundSystem:

    def __init__(self):
        self.dist = dict()
        self.stt = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.stt[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station,time = self.stt[id]
        if station not in self.dist: self.dist[station] = dict()
        if stationName not in self.dist[station]: self.dist[station][stationName] = (0,0)
        total,cnt = self.dist[station][stationName]
        self.dist[station][stationName] = (total+t-time,cnt+1)
        del self.stt[id]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        x,y = self.dist[startStation][endStation]
        return x/y


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)