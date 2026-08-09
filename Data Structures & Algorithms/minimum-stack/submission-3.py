
class MinStack:

    def __init__(self):
        self.heap=[]
        self.sor=[]

    def push(self, val: int) -> None:
        self.heap.append(val)
        self.sor=sorted(self.heap)

    def pop(self) -> None:
        self.sor=sorted(self.heap)
        x=self.heap.pop()
        self.sor.remove(x)
        

    def top(self) -> int:
        return self.heap[-1]

    def getMin(self) -> int:
        return self.sor[0]
