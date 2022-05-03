"""
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}

        for i, num in enumerate(nums):
            if target - num in num_map:
                return [num_map[target - num], i]
            num_map[num] = i
