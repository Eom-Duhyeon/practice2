"""
높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

height = [0,1,0,2,1,0,1,3,2,1,2,1]

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 예외처리
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        #투 포인터 방식. left와 right 포인터를 좁히면서 값을 구해간다.

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume

S = Solution()
print(S.trap(height))