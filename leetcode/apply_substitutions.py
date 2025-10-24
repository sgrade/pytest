# 3481. Apply Substitutions
# https://leetcode.com/problems/apply-substitutions/

from typing import List


replacements = [["P","jluwndp"],["U","%P%%P%qi"]]
text = "%U%_%P%"

class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        mp = dict(replacements)
        return self.replace(text, mp)

    def replace(self, text, mp):
        ans = ''
        lo = 0
        
        while lo < len(text):
            if text[lo] == '%':
                hi = text.find('%', lo + 1) # Assume that there is a closing %
                key = text[lo + 1:hi]
                if key in mp:
                    ans += self.replace(mp[key], mp)
                else:
                    ans += text[lo]
                lo = hi + 1
            else:
                ans += text[lo]
                lo += 1
        
        return ans
            

print(Solution().applySubstitutions(replacements, text))
