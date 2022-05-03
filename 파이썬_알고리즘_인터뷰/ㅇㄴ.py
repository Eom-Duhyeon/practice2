class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            # 우리는 prev를 return할거다
            prev.next = b

            # 이제 다음을 위해 head와 prev의 위치를 당겨준다. head는 변하는 과정에서 이미 한 번 당겨졌다.
            head = head.next
            prev = prev.next.next

        return root.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
c = Solution()
d = c.swapPairs(node1)
while d:
    print(d.val)
    d.next = d