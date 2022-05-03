"""
숫자 집합을 조합하여 합이 target이 되는 원소를 나열하라. 각 원소는 중복으로 나열 가능하다.
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""


class Solution(object):
    def mysolution(self, candidates, target):
        pass

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result
