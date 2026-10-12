class MinStack:

    def __init__(self):
        self.minimum = float('inf')
        self.min_stack = []
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if val < self.minimum:
            self.min_stack.append(val)
            self.minimum = val
        else:
            self.min_stack.append(self.minimum)

    def pop(self) -> None:
        self.arr.pop()
        self.min_stack.pop()
        if self.min_stack:
            self.minimum = self.min_stack[-1]
        else:
            self.minimum = float('inf')

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
