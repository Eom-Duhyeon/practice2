"""
[from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라. 여러 일정이 있는 경우
사전 어휘 순으로 방문한다.

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
"""
import collections


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b) #편해보인다 다시 읽어보자

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append((graph[stack[-1]].pop(0)))
            route.append(stack.pop())
        return route[::-1]
