# 2043. Simple Bank System
# https://leetcode.com/problems/simple-bank-system/

from typing import List


class Bank:
    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.balance = [0] + balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.n or account2 > self.n or self.balance[account1] < money:
            return False
        self.balance[account1] -= money
        self.balance[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self.n:
            return False
        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.n or self.balance[account] < money:
            return False
        self.balance[account] -= money
        return True 


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)


if __name__ == "__main__":
    inputs = [[[20,1000,500,40,90]],[3,400],[1,2,30],[10,50]]
    transactions = ["Bank","deposit","transfer","withdraw"]
    bank = Bank(inputs[0][0])
    for i in range(1, len(inputs)):
        if transactions[i] == "deposit":
            output = bank.deposit(inputs[i][0], inputs[i][1])
        elif transactions[i] == "transfer":
            output = bank.transfer(inputs[i][0], inputs[i][1], inputs[i][2])
        elif transactions[i] == "withdraw":
            output = bank.withdraw(inputs[i][0], inputs[i][1])
        print(output)
