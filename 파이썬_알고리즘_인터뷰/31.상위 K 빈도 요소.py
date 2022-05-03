"""
K번 이상 등장하는 요소를 추출하라.
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
import collections
import heapq


class Solution(object):
    def mysolution(self, nums, k):
        a = collections.Counter(nums)
        result = []
        for index, val in a.items():
            if val >=k:
                result.append(index)
        print(result) #개선 필요

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqs = collections.Counter(nums)
        freqs_heap=[]
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk