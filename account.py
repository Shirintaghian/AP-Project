class Account:
    balance = 0
    transactions = []
    def __init__(self, alias: str, nid: str, password: str):
        self.alias = alias
        self.nid = nid
        self.password = password

class User:
    accs = []
    def __init__(self, name: str, nid: str, password: str, phone: str, email: str):
        self.name = name
        self.nid = nid
        self.password = password
        self.phone = phone
        self.email = email

class Transaction:
    def __init__(self, amount: int, tType: str):
        self.amount = amount
        self.tType = tType