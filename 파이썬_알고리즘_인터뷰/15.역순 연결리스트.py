"""
연결리스트를 뒤집어라
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        prev = None
        # prev를 리턴할거다

        while node:
            next, node.next = node.next, prev
            # next라는 버퍼에 node.next를 저장하고
            # 노드의 다음 부분은 prev를 연결
            prev, node = node, next
            # prev는 반복문 돌린 수 만큼 역순된 elements가 연결된 노드
            # node는 반복문만큼 앞부분이 없는 next(그러니까 node)

        return prev