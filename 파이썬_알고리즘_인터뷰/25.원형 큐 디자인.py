"""
원형 큐를 디자인하라
"""


class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [None] * k
        self.maxlen = k
        self.front = 0  # pop시 front 변경
        self.rear = 0  # push시 rear가 변경

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None  # 이 함수는 dequeue에서 반환을 하지 않는다. 그저 없앤다
            self.front = (self.front + 1) % self.maxlen
            return True

    def Front(self):
        """
        :rtype: int
        """
        return -1 if self.q[self.front] is None else self.q[self.front]

    def Rear(self):
        """
        :rtype: int
        """
        return -1 if self.q[self.rear] is None else self.q[self.rear - 1]  # enqueue할 때 마지막에 rear를 늘려줬음을 기억하자

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self):
        """
        :rtype: bool
        """
        return self.front == self.rear and self.q[self.front] is not None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()