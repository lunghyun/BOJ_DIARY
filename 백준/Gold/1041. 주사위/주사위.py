class Dice:
    def __init__(self):
        self.numList = list
        self.list = list
        
    def setDice(self):
        self.n = int(input())
        self.numList = list(map(int, input().split()))
    
    def minimum(self):
        if self.n == 1:
            s = sum(self.numList)
            m = max(self.numList)
            return(s - m)
        else:        
            self.list = []
            total = 0
            
            self.list.append(min(self.numList[0], self.numList[5]))
            self.list.append(min(self.numList[1], self.numList[4]))
            self.list.append(min(self.numList[2], self.numList[3]))
            self.list = sorted(self.list)
            
            total += (self.list[0])*(self.n-2)*(5*self.n-6)
            total += (self.list[0]+self.list[1])*(2*self.n-3)*4
            total += (self.list[0]+self.list[1]+self.list[2])*4
            return total
player = Dice()
player.setDice()
print(player.minimum())
#       4
#   5   1   2   6
#       3