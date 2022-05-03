"""
연결 리스트가 팰린드롬 구조인지 판별하라
Input: head = [1,2,2,1]
Output: true
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections

class Another_Solution(object):
    def runner(self, head):
        rev = None
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        #만약 fast가 남아있다면, 즉 리스트가 홀수개라면
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        return no rev

class Solution(object):
    def isPalindrome(self, head):
        # 예외처리
        if not head:
            return True
        q = collections.deque()
        node = head

        while node:
            q.append(node.val)
            node = node.next
        while len(q) > 1:
            if q.popleft() != q.pop():
                return false
        return True
        """
        :type head: ListNode
        :rtype: bool
        """