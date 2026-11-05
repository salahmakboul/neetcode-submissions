class MinStack:

    def __init__(self):
        self.mnstk =[]
        self.minstk=[]
        

    def push(self, val: int) -> None:
        self.mnstk.append(val)
        if (not self.minstk )or( val <= self.minstk[-1]) :
            self.minstk.append(val)
        else :
            self.minstk.append(self.minstk[-1])
        
        

    def pop(self) -> None:
        self.mnstk.pop()
        self.minstk.pop()
        


    def top(self) -> int:
        return self.mnstk[-1]
        

    def getMin(self) -> int:
        return self.minstk[-1]
        
