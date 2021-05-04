class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q=collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)  # 3 2 1 4
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())  # 4 3 2 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()





# Time - pop, peek, empty - O(1), Push - O(N)
# Space - O(1)
