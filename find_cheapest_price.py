"""
There are n cities connected by m flights. Each flight
starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting
city src and the destination dst, your task is to find the cheapest price
from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
"""

from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, stops: int) -> int:
        adjlist = defaultdict(list)
        stops += 1

        for u, v, w in flights:
            adjlist[u].append((v, w))

        pq = []
        seen = {}
        heapq.heappush(pq, (0, 0, src))
        seen[(src, 0)] = 0

        while len(pq) > 0:
            dist, k, city = heapq.heappop(pq)
            if city == dst:
                return dist

            if seen[(city, k)] < dist:
                continue

            for v, w in adjlist[city]:
                if k + 1 <= stops and ((v, k + 1) not in seen or seen[(v, k + 1)] > dist + w):
                    heapq.heappush(pq, (dist + w, k + 1, v))
                    seen[(v, k + 1)] = dist + w

        return -1