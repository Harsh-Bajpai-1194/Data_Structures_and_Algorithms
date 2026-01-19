from typing import List
class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance
        self.num_accounts = len(balance)
    def _is_valid_account(self, account: int) -> bool:
        return 1 <= account <= self.num_accounts
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (self._is_valid_account(account1) and self._is_valid_account(account2)): return False
        if self.balance[account1 - 1] >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        else: return False
    def deposit(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account): return False
        self.balance[account - 1] += money
        return True
    def withdraw(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account): return False
        if self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        else: return False