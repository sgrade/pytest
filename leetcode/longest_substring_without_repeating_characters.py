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

        # Runtime: 76 ms
        # Your runtime beats 99.20 % of python3 submissions.

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:

            # РАЗОБРАЛСЯ, НО НАДО ВОСПРОИЗВЕСТИ ТО ЖЕ САМОЕ САМОМУ
            # https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

            no_of_chars = 256
            n = len(s)
            cur_len = 1  # To store the lenght of current substring
            max_len = 1  # To store the result
            # prev_index = 0  # To store the previous index
            i = 0

            # Initialize the visited array as -1, -1 is used to indicate
            # that character has not been visited yet.
            visited = [-1] * no_of_chars

            # Mark first character as visited by storing the index of
            # first character in visited array.
            visited[ord(s[0])] = 0

            # Start from the second character. First character is already
            # processed (cur_len and max_len are initialized as 1, and
            # visited[str[0]] is set
            for i in range(1, n):
                prev_index = visited[ord(s[i])]

                # If the currentt character is not present in the already
                # processed substring or it is not part of the current NRCS,
                # then do cur_len++
                if prev_index == -1 or (i - cur_len > prev_index):
                    cur_len += 1

                # If the current character is present in currently considered
                # NRCS, then update NRCS to start from the next character of
                # previous instance.
                else:
                    # Also, when we are changing the NRCS, we should also
                    # check whether length of the previous NRCS was greater
                    # than max_len or not.
                    if cur_len > max_len:
                        max_len = cur_len

                    cur_len = i - prev_index

                # update the index of current character
                visited[ord(s[i])] = i

            # Compare the length of last NRCS with max_len and update
            # max_len if needed
            if cur_len > max_len:
                max_len = cur_len

            return max_len


        """NOT FINISHED"""
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
        """


sol = Solution()

inp = "abcabcbb"
print("expected 3, got", sol.lengthOfLongestSubstring(inp))
"""

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
"""