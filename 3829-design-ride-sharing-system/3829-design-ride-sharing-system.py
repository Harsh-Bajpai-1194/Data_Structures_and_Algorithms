class RideSharingSystem(object):
    from collections import deque
    def __init__(self):
        self.a,self.b,self.c=deque(),deque(),set()

    def addRider(self, riderId):
        """
        :type riderId: int
        :rtype: None
        """
        self.b.append(riderId),self.c.add(riderId);

    def addDriver(self, driverId):
        """
        :type driverId: int
        :rtype: None
        """
        self.a.append(driverId)

    def matchDriverWithRider(self):
        """
        :rtype: List[int]
        """
        if not self.a: return [-1]*2
        else:
            while (self.b):
                rider=self.b.popleft()
                if rider in self.c:
                    self.c.remove(rider)
                    driver=self.a.popleft();return [driver,rider];
        return [-1]*2
                    
    def cancelRider(self, riderId):
        """
        :type riderId: int
        :rtype: None
        """
        if riderId in self.c: self.c.remove(riderId)

# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)