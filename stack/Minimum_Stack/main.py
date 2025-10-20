class MinStack:

    def __init__(self):
        # The stack will store tuples of (value, current_minimum)
        self.stack = []

    def push(self, val: int) -> None:
        # If the stack is empty, the new value is also the new minimum.
        # Otherwise, the new minimum is the smaller of the new value and the current minimum.
        if not self.stack:
            new_min = val
        else:
            new_min = min(val, self.getMin())
        self.stack.append((val, new_min))

    def pop(self) -> None:
        # Assuming pop is only called on a non-empty stack, as per typical problem constraints.
        self.stack.pop()

    def top(self) -> int:
        # Returns the value part of the tuple at the top of the stack.
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Returns the minimum part of the tuple at the top of the stack.
        # This is now an O(1) operation.
        return self.stack[-1][1]
