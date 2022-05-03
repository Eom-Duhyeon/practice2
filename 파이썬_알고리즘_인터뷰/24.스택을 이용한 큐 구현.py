"""
스택을 이용해 다음 연산을 지원하는 큐를 구현하라.
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]
"""


class MyQueue(object):

    def __init__(self):
        self.input=[]
        self.output=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.output.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        return self.output[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return self.input==[] and self.output==[]