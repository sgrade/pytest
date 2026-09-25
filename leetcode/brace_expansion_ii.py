# 1096. Brace Expansion II
# https://leetcode.com/problems/brace-expansion-ii/


# Based on Editorial's Approach 2: Stack
class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        operator_stack = []
        operand_stack = []

        def apply_operator() -> None:
            right = operand_stack.pop()
            left = operand_stack.pop()

            if operator_stack.pop() == "+":
                operand_stack.append(left | right)
            else:
                operand_stack.append(
                    {prefix + suffix for prefix in left for suffix in right}
                )

        for index, character in enumerate(expression):
            follows_operand = index > 0 and (
                expression[index - 1] == "}"
                or expression[index - 1].isalpha()
            )

            if character == ",":
                # Concatenation has higher precedence than union.
                while operator_stack and operator_stack[-1] == "*":
                    apply_operator()
                operator_stack.append("+")
            elif character == "{":
                if follows_operand:
                    operator_stack.append("*")
                operator_stack.append("{")
            elif character == "}":
                while operator_stack[-1] != "{":
                    apply_operator()
                operator_stack.pop()
            else:
                if follows_operand:
                    operator_stack.append("*")
                operand_stack.append({character})

        while operator_stack:
            apply_operator()

        return sorted(operand_stack[-1])
