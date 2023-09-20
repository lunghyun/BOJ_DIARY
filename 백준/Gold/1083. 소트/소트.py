class Sorted:
    def __init__(self):
        self.n = 0
        self.aList = []
        self.s = 0
        
    def setList(self):
        self.n = int(input())
        self.aList = list(map(int, input().split()))
        self.s = int(input())
    
    def printList(self):
        # print(", ".join(map(str, self.aList)))
        print(*self.aList)
        
    def sortList(self):
        # * print(list[0:4])
        # 결과 : [1,2,3,4]
        i=0
        while i < self.n and self.s > 0:
            mxPos = self.aList.index(max(self.aList[i:i+self.s+1]))
            if mxPos != i:
                self.aList[mxPos], self.aList[mxPos-1] = self.aList[mxPos-1], self.aList[mxPos]    
                self.s -= 1
            else:
                i+=1
                    
        self.printList()
            
        
player = Sorted()
player.setList()
player.sortList()