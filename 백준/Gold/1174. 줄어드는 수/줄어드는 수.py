class Decrease:
    def __init__(self):
        self.n = 0
    
    def setDec(self):
        self.n = int(input())
        
    def backT(self, n, sList):
        sList.append(int(n))
        for i in range(0, int(n[-1])):
            self.backT(n + str(i), sList)
        
    def calDNum(self):
        if self.n > 1023:
            print(-1)
            return
        
        sList = []
        for i in range(10):
            self.backT(str(i) ,sList)
        
        print(sorted(sList)[self.n-1])
        
player = Decrease()
player.setDec()
player.calDNum()