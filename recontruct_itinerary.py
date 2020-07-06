"""
Given a list of airline tickets represented by pairs of departure and arrival
airports [from, to], reconstruct the itinerary in order. All of the tickets
belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary
that has the smallest lexical order when read as a single string.
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        mapping = {}
        for start, end in tickets:
            if start in mapping:
                mapping[start].append(end)
            else:
                mapping[start] = [end]
        # sort the list in descending order and pop from the last list
        for src in mapping.keys():
            mapping[src].sort(reverse=True)

        # we have a stack to know the cur the next node
        stack = ["JFK"]
        result = []

        while len(stack) > 0:
            cur = stack[-1]
            # check whether it has ticket, it has, add to stack
            if cur in mapping and len(mapping[cur]) > 0:
                stack.append(mapping[cur].pop())
            else:
                result.append(stack.pop())
            # since the result starts from destination, we reverse it
        return result[::-1]
