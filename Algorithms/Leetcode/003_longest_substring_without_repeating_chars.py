"""
    Given a string, find the length of the longest substring without repeating characters.
"""


class Solution:
    def get_longest_substring(self, s):
        start, length, n = 0, 0, len(s)
        hashmap = {}
        for i in range(n):
            start = max(start, hashmap.get(s[i], -1) + 1)
            length = max(length, i - start + 1)
            hashmap[s[i]] = i

        return length


given_str = 'pwwkev'

get_length = Solution()
print(get_length.get_longest_substring(given_str))
