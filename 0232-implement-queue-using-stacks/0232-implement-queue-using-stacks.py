class MyQueue:

    def __init__(self):
        self.Q = deque()

    def push(self, x: int) -> None:
        self.Q.append(x)

    def pop(self) -> int:
        try:
            return self.Q.popleft()
        except:
            return None
    def peek(self) -> int:
        try:
            return self.Q[0]
        except:
            return None

    def empty(self) -> bool:
        return not self.Q


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()