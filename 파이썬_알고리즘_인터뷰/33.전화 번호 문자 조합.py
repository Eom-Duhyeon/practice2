"""
2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라.
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
       "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
"""

class Solution(object):
    def mysolution(self, digits):
        result=[]
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        dfs(0, "")

        return result

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, path + j)

        if not digits:
            return

        result = []
        dfs(0, "")
        return result

