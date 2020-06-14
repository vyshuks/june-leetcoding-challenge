"""
Given a set of distinct positive integers, find the largest
subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        results = []
        if n == 0:
            return results
        nums.sort()
        next_index = [-1] * n
        sizes = [1] * n
        max_len = 1
        max_index = 0

        for i in range(n - 1, -1, -1):
            j = i + 1
            _max, _max_index = 0, i

            while j < n:
                if nums[j] % nums[i] == 0 and sizes[j] > _max:
                    _max_index = j
                    _max = sizes[j]
                j += 1

            if _max_index != i:
                sizes[i] += sizes[_max_index]
                next_index[i] = _max_index
                if _max + 1 > max_len:
                    max_len = _max + 1
                    max_index = i

        curr = max_index
        while curr >= 0:
            results.append(nums[curr])
            curr = next_index[curr]

        return results