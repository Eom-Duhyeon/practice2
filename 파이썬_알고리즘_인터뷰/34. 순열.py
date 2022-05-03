"""
서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
import itertools


class Solution(object):
    def mysolution(self, nums):
    # 1. itertools 이용. 리스트(nums)의 순열을 튜플 형태로 반환
    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        return list(itertools.permutations(nums))

    # 2. dfs 이용
    def premute(self, nums):
        result = []
        prev_elements = []
        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:]) # 의미없는 슬라이싱은 아니다 참조가 아니라 복사를 위해

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result

c = Solution()
nums = [1,2,3]
print(c.premute([1,2,3]))
