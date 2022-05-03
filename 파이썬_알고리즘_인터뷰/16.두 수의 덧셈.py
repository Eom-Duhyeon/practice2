"""
역순으로 저장된 연결 리스트의 숫자를 더하라
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
"""


class Solution(object):
    def reverseList(self, head):
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        66return prev

    def toList(self, node):
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    def toLinkedlist(self, result):
        prev = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        result = int(''.join(str(e) for e in a)) + int(''.join(str(p) for p in b))
        return self.toLinkedlist(str(result))
