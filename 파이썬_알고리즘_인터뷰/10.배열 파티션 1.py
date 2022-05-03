"""
n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
"""


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n

        return sum