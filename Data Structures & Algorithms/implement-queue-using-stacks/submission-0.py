class MyQueue:

    def __init__(self):
        self.inputStack = []
        self.outputStack=[]
        

    def push(self, x: int) -> None:
        self.inputStack.append(x)


    def pop(self) -> int:
        ##this reverse teh order of the stack
        if self.outputStack :
            while self.inputStack :
                self.outputStack.append(self.inputStack.pop())
        return self.outputStack.pop()
        
    def peek(self) -> int:
        if not self.outputStack :
            while self.inputStack :
                self.outputStack.append(self.inputStack.pop())
        return self.outputStack[-1]
        

    def empty(self) -> bool:
        return not self.outputStack and not self.inputStack        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()