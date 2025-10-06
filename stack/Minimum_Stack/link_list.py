class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class MinStack:

    def __init__(self):
        self.head = None
        self.size = 0
        
    def push(self, val: int) -> None:
        new_node = Node(val)
        if self.head:
          new_node.next = self.head
        self.head = new_node
        self.size += 1
        
    def pop(self) -> None:
        if (self.head == None):
            return ("Stack is empty")
        if self.head:
            self.head = self.head.next
        self.size -= 1

    def top(self) -> int:
        if (self.head == None):
            return ("Stack is empty")
        return (self.head.value)

    def getMin(self) -> int:
        if (self.head == None):
            return ("Stack is empty")
        min_val = self.head.value
        current = self.head
        while current is not None:
            if min_val > current.value:
                min_val = current.value
            current = current.next
        return min_val  
