"""
정렬되어 있는 두 연결 리스트를 합쳐라.
"""

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # list1이 다 떨어져버렸거나 list1의 값이 더 커 list2부터 정렬해야 한다면 서로 교환
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1


        # list1.next는 재귀를 통해 결정
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)

        # list2 까지 합쳐진 list1을 반환한다.
        return list1