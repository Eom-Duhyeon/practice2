"""
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        p = 1
        for i in nums:
            output.append(p)
            p = p * i

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]

        return output