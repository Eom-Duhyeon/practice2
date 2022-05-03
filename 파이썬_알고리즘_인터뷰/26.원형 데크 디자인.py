import collections


class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.dq = collections.deque(maxlen=self.k)

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.dq) >= self.k:
            return False

        else:
            self.dq.appendleft(value)
            return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.dq) >= self.k:
            return False

        else:
            self.dq.append(value)
            return True


    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.dq:
            self.dq.popleft()
            return True
        else:
            return False


    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.dq:
            self.dq.pop()
            return True
        else:
            return False


    def getFront(self):
        """
        :rtype: int
        """
        if self.dq:
            return self.dq[0]
        else:
            return -1


    def getRear(self):
        """
        :rtype: int
        """
        if self.dq:
            return self.dq[-1]
        else:
            return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.dq:
            return False
        else:
            return True

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.dq)==self.k:
            return True
        else:
            return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

