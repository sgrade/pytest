# format-leetcode

Review the code and apply the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) with the following exceptions:
- Do NOT change the name and the signature of the classes and functions given in the LeetCode problem statement except type annotations.
- Module-level docstrings are OPTIONAL (the problem number and URL comment at the top is sufficient).
- Class and method docstrings are OPTIONAL for LeetCode solution classes and their methods.
- Short variable names (ans, res, curr, prev, etc.) are ACCEPTABLE when their meaning is clear from context.
- Line length follows Google's 80-character recommendation (configured in pyproject.toml).
- LeetCode method names use camelCase (as specified by LeetCode), but helper functions and variables should use snake_case.

## Standard Problem Annotation

Ensure the file starts with exactly this format (note: 2 blank lines before class per PEP 8):
```
# [number]. [Problem Title]
# https://leetcode.com/problems/[problem-slug]/


# [Optional comment about approach]
class Solution:
```

Example:
```
# 3453. Separate Squares I
# https://leetcode.com/problems/separate-squares-i/


# Based on Editorial's Approach 1: Binary Search
class Solution:
```
