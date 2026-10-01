# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c == "(" or c == "[" or c == "{" or not st:
                st.append(c)
            elif st[-1] == "(" and c == ")":
                st.pop()
            elif st[-1] == "[" and c == "]":
                st.pop()
            elif st[-1] == "{" and c == "}":
                st.pop()
            else:
                st.append(c)
        if st:
            return False
        return True
