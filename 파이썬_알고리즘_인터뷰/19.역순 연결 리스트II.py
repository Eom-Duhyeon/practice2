"""
인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
"""

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        #예외처리
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head

        for i in range(right-1):
            start = start.next
        end = start.next

        for _ in range(left - right):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next