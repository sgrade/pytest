# 3606. Coupon Code Validator
# https://leetcode.com/problems/coupon-code-validator/


class Solution:
    def validateCoupons(
        self, code: list[str], businessLine: list[str], isActive: list[bool]
    ) -> list[str]:
        valid_coupons: dict[str, list[str]] = {
            "electronics": [],
            "grocery": [],
            "pharmacy": [],
            "restaurant": [],
        }

        for i in range(len(code)):
            if not isActive[i]:
                continue
            if not businessLine[i] in valid_coupons:
                continue
            if not code[i]:
                continue
            code_valid: bool = True
            for ch in code[i]:
                if not ch.isalnum():
                    if ch == "_":
                        continue
                    code_valid = False
                    break
            if code_valid:
                valid_coupons[businessLine[i]].append(code[i])

        ans: list = []
        for business_line in sorted(valid_coupons.keys()):
            if valid_coupons[business_line]:
                ans.extend(sorted(valid_coupons[business_line]))
        return ans
