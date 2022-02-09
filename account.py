class Account:
    balance = 0
    transactions = []
    def __init__(self, alias: str, nid: str, password: str):
        self.alias = alias
        self.nid = nid
        self.password = password

class User:
    def __init__(self, nid: str, password: str):
        self.nid = nid
        self.password = password

class Transaction:
    def __init__(self, amount: int, tType: str):
        self.amount = amount
        self.tType = tType