class Cell:

    def __init__(self, x, y, status):
        self.x = x
        self.y = y
        self.status = status

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getStatus(self):
        return self.status

    def setStatus(self, stat):
        self.status = stat
