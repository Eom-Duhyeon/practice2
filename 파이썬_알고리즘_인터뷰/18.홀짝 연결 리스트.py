"""
연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라.
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
"""

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return head