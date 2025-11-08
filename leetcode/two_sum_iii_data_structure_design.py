# 170. Two Sum III - Data structure design
# https://leetcode.com/problems/two-sum-iii-data-structure-design/


class TwoSum:
    def __init__(self):
        self.cntr = {}

    def add(self, number: int) -> None:
        if number in self.cntr:
            self.cntr[number] += 1
        else:
            self.cntr[number] = 1

    def find(self, value: int) -> bool:
        for num in self.cntr.keys():
            target = value - num
            if target != num:
                if target in self.cntr:
                    return True
            elif self.cntr[target] > 1:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
