"""
https://leetcode.com/problems/longest-common-prefix/description/
Write a function to find the longest common prefix string amongst an array of strings
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs:
            prefix = str()
            longest_found = False

            for letter in strs[0]:
                if longest_found:
                    break
                else:
                    print('letter:', letter)
                    prefix += letter
                    print('prefix:', prefix)
                    for element in strs:
                        if element.startswith(prefix):
                            continue
                        else:
                            prefix = prefix[:-1]
                            longest_found = True
                            break

            return prefix
        else:
            return ""


input_data = ['pazpple', 'pazirbus', 'pazndroid']
x = Solution()
print(x.longestCommonPrefix(input_data))
