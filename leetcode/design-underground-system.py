# 1396. Design Underground System
# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.averages = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_station, checkin_time = self.checkins[id]
        travel_time = t - checkin_time
        stations = checkin_station + '-' + stationName
        if stations in self.averages:
            self.averages[stations][0] += travel_time
            self.averages[stations][1] += 1
        else:
            self.averages[stations] = [travel_time, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        stations = startStation + '-' + endStation
        return self.averages[stations][0] / self.averages[stations][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
