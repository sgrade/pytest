# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # get the first longest substring without repeating characters
        def get_substring(string):
            if len(string) == 0:
                return 0
            elif len(string) == 1:
                return 1
            else:
                hash_list = list()
                for char in string:
                    if char in hash_list:
                        return len(hash_list)
                    else:
                        hash_list.append(char)
            # if the whole string has no repeating characters
            return len(string)

        # get the first substing without repeating characters
        current_len = get_substring(s)

        # there might be longer substring in the rest of the original string
        length = len(s)
        if length > current_len:

            substring_to_test = s[current_len:]
            while substring_to_test:
                candidate_len = get_substring(substring_to_test)
                if candidate_len > current_len:
                    # print(candidate_len)
                    substring_to_test = substring_to_test[candidate_len:]
                    current_len = candidate_len
                else:
                    break

        return current_len


sol = Solution()

inp = "abcabcbb"
print("expected 3, got", sol.lengthOfLongestSubstring(inp))

inp = "bbbbbbbb"
print("expected 1, got", sol.lengthOfLongestSubstring(inp))

inp = "pwwkew"      # expected 3
print("expected 3, got", sol.lengthOfLongestSubstring(inp))

inp = "au"
print("expected 2, got", sol.lengthOfLongestSubstring(inp))

inp = "aab"
print("expected 2, got", sol.lengthOfLongestSubstring(inp))

inp = "dvdf"
print("expected 3, got", sol.lengthOfLongestSubstring(inp))
