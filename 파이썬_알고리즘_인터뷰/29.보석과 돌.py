"""
J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다.
"""
import collections


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        return sum(s in jewels for s in stones)
        # s in jewels for s in stones 하면 true와 false의 결과로 나온다. sum은 true를 1로 잡아 합산한다.
    def numJwelsInstones1(self, jewels, stones):
        freqs = collections.defaultdict(int)
        count = 0

        for char in stones:
            freqs[char] += 1

        for _ in J:
            count += freqs[char]
            return count

    def much_shorter(self, jewels, stones):
        freqs = collections.Counter(stones)
        count = 0

        for char in jewels:
            count +=freqs[char]

        return count
