def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    result = ''

    def expand(left, right):
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1] #while문이 검토하고 밑에서 조건추가라 left +1, right -1 꼭

    if len(s) < 2 or s == s[::-1]:
        return s

    for i in range(len(s) - 1):
        result = max(result, \
                     expand(i, i + 1), \ #팰린드롬이 짝수일 경우
                     expand(i, i + 2), \ #팰린드롬이 홀수일 경우
                     key=len) #max 기준은 문자열

    return result