class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
    def pop(self) -> None:
        if not self.stack:
            return ("Stack is empty")
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return ("Stack is empty")
        return (self.stack[-1])

    def getMin(self) -> int:
        if not self.stack:
            return ("Stack is empty")
        min_val = self.stack[0]
        for val in self.stack:
            if val < min_val:
                min_val = val
        return (min_val)
