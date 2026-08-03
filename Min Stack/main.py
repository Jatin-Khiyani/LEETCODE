# Incomplete


class MinStack:
    def __init__(self):

        self.stack = []
        self.head = 0
        self.minimum = 0
        self.mini_stack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """

        self.stack.append(value)

        if not self.mini_stack:  # noqa: SIM114
            self.minimum = value
            self.mini_stack.append(value)
        elif value < self.minimum:
            self.minimum = value
            self.mini_stack.append(value)
        self.head += 1

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[self.head - 1] == self.minimum:
            self.mini_stack.pop()
            self.minimum = self.mini_stack[self.head - 1]
        self.stack.pop()

        self.head -= 1

    def top(self):
        """
        :rtype: int
        """
        head = self.stack[self.head - 1]
        return head

    def getMin(self):
        """
        :rtype: int
        """
        minimum = self.minimum
        return minimum


# Your MinStack object will be instantiated and called as such:

minStack = MinStack()
minStack.push(-2)
print("Minimum. After Pussying -2 ", minStack.getMin())
minStack.push(0)
minStack.push(-3)
print("Minimum. After Pussying -3 ", minStack.getMin())
print(minStack.stack)
print(minStack.mini_dict)
minStack.getMin()
minStack.pop()
print("Minimum. After Pooping -3 ", minStack.getMin())
print(minStack.stack)
print(minStack.mini_dict)
minStack.top()
minStack.getMin()
