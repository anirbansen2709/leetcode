class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:

        while self.stack1:
          element =  self.stack1.pop()
          self.stack2.append(element)

        self.stack1.append(x)

        while self.stack2:
          element =  self.stack2.pop()
          self.stack1.append(element)

    def pop(self) -> int:
        
        element = self.stack1.pop()
        return element

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        return True if not self.stack1 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# TC - O(n)
# SC - O(n)
