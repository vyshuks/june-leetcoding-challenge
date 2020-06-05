"""
Given an array w of positive integers, where w[i] describes the
weight of index i, write a function pickIndex which randomly picks
an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
"""


class Solution:

    def __init__(self, w: List[int]):
        total = 0
        self.prefix = []
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total_sum = total

    def pickIndex(self) -> int:
        random_num = self.total_sum * random.random()
        low, high = 0, len(self.prefix)
        while low < high:
            mid = low + (high - low) // 2
            if random_num > self.prefix[mid]:
                low = mid + 1
            else:
                high = mid
        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()