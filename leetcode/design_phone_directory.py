# 379. Design Phone Directory
# https://leetcode.com/problems/design-phone-directory/


class PhoneDirectory:
    """Track available phone numbers using a set for O(1) operations."""

    def __init__(self, maxNumbers: int):
        self.available = set(range(maxNumbers))

    def get(self) -> int:
        if not self.available:
            return -1
        return self.available.pop()

    def check(self, number: int) -> bool:
        return number in self.available

    def release(self, number: int) -> None:
        self.available.add(number)
