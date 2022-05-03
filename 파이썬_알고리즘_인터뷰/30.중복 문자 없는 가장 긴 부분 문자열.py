"""
중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라.
입력
"abcbcbb"
출력
3


만약 브루트하게 푼다면 앞을 바라보는 방식으로 문자열의 위치 i에 따라 항상 재검토해야 한다.
해시(dictionary)를 이용해 문자열이 나왔던 인덱스를 값으로 갱신한다. 이미 검토했던 sub문자열에 대해 겹치는 문자가 나오면
원래 있었던 문자의 index +1의 위치부터 i까지의 길이를 잰다.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_length = 0
        used = {}
        for index, char in enumerate(s):
            if char in used and start <= used[char]: #start는 substring의 시발점이다. start가 used[char] 앞에 있다면
                                                     # 바로 max_length를 구하러 가도 된다. 입력에 "tmmzuxt"를 넣어보자
                start = used[char] +1
            else:
                max_length = max(max_length, index - start +1)
            used[char] = index

        return max_length