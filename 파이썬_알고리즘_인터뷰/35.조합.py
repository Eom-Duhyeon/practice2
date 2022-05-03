"""
전체 수 n을 입력받아 k개의 조합을 리턴하라.
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
import itertools


class Solution(object):

    #itertools 이용
    def combine1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(itertools.combinations(range(1, n+1), k))

    def combine(self, n, k):
        result = []
        def dfs(elements, start, k):
            if k==0:
                results.append(elements[:])

            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()

        dfs([], 1, k)
        return result
