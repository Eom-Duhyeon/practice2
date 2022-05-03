"""
연결 리스트를 입력받아 페어 단위로 스왑하라.
Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""


class Solution(object):
    def swapPairs_1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
        return head

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = ListNode(None)
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

        # 우리는 prev를 return할거다
        prev.next = b

        #이제 다음을 위해 head와 prev의 위치를 당겨준다. head는 변하는 과정에서 이미 한 번 당겨졌다.
        head=head.next
        prev = prev.next.next

        return prev.next