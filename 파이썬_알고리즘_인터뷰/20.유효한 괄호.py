"""
괄호로 된 입력값이 올바른지 판별하라.
Input: s = "()[]{}"
Output: true
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        table = {
            ')' : '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        return len(stack) == 0