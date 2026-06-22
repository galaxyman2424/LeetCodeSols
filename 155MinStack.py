class MinStack:

    def __init__(self):
        self.mstack = []

    def push(self, value: int) -> None:
        if not self.mstack:
            current_min = value
        else:
            current_min = min(value, self.mstack[-1][1])
            
        self.mstack.append((value, current_min))

    def pop(self) -> None:
        self.mstack.pop()

    def top(self) -> int:
        return self.mstack[-1][0]

    def getMin(self) -> int:
        return self.mstack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()