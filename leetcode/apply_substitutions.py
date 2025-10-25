# 3481. Apply Substitutions
# https://leetcode.com/problems/apply-substitutions/

from typing import List
from functools import lru_cache


class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        mp = dict[str, str](replacements)
        
        @lru_cache(maxsize=None)
        def replace(text):
            result = []
            i = 0
            
            while i < len(text):
                if text[i] == '%':
                    j = text.find('%', i + 1)
                    key = text[i + 1:j]
                    if key in mp:
                        result.append(replace(mp[key]))
                    i = j + 1
                else:
                    result.append(text[i])
                    i += 1
            
            return ''.join(result)
        
        return replace(text)
