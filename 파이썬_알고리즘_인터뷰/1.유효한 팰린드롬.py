"""
주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
"""

def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]