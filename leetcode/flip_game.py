# 293. Flip Game
# https://leetcode.com/problems/flip-game/


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> list[str]:
        states = []
        for i in range(len(currentState) - 1):
            if currentState[i] == "+" and currentState[i + 1] == "+":
                next_state = currentState[:i] + "--" + currentState[i + 2 :]
                states.append(next_state)
        return states
