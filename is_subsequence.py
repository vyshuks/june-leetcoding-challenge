"""
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the
original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters.
(ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and
you want to check one by one to see if T has its subsequence.
In this scenario, how would you change your code?

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s_len == 0:
            return True

        s_ptr = 0

        for i in range(t_len):
            if s[s_ptr] == t[i]:
                s_ptr += 1
            if s_ptr == s_len:
                return True

        return s_ptr == s_len