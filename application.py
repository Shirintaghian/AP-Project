import time
from database import Table, Field
from account import Account, User, Transaction

users = []
tableList = []

def insertRecord(cmds):
    tableName = cmds[3]
    fields = cmds[5]
    fields = fields.replace('(', '')
    fields = fields.replace(')', '')
    fields = fields.replace(';', '')
    fieldValues = fields.split(',')

    for table in tableList:
        if table.name == tableName:
            if len(fieldValues) == len(table.fields):
                table.insert(fieldValues)
                table.updateFile()
            else:
                print("wrong number of fields")    

def updateRecord(cmds):
    tableName = cmds[2]
    fields = None
    conditions, orCond, andCond = [], False, False
    if "OR" in cmds:
        conditions = [cmds[4], cmds[6]]
        orCond = True
        fields = cmds[8]
    elif "AND" in cmds:
        conditions = [cmds[4], cmds[6]]
        andCond = True
        fields = cmds[8]
    else:
        conditions = [cmds[4]]
        fields = cmds[6]
    
    fields = fields.replace('(', '')
    fields = fields.replace(')', '')
    fields = fields.replace(';', '')
    fieldValues = fields.split(',')

    for table in tableList:
        if table.name == tableName:
            if len(fieldValues) == len(table.fields):
                table.update(fieldValues, conditions, andCond, orCond)
                table.updateFile()
            else:
                print("wrong number of fields") 

def deleteRecord(cmds):
    tableName = cmds[3]
    conditions, orCond, andCond = [], False, False
    if "OR" in cmds:
        conditions = [cmds[5], cmds[7].replace(';', '')]
        orCond = True
    elif "AND" in cmds:
        conditions = [cmds[5], cmds[7].replace(';', '')]
        andCond = True
    else:
        conditions = [cmds[5].replace(';', '')]
    
    for table in tableList:
        if table.name == tableName:
            table.delete(conditions, andCond, orCond)
            table.updateFile()

def selectRecord(cmds):
    tableName = cmds[3]
    conditions, orCond, andCond = [], False, False
    if "OR" in cmds:
        conditions = [cmds[5], cmds[7].replace(';', '')]
        orCond = True
    elif "AND" in cmds:
        conditions = [cmds[5], cmds[7].replace(';', '')]
        andCond = True
    else:
        conditions = [cmds[5].replace(';', '')]
    
    for table in tableList:
        if table.name == tableName:
            table.select(conditions, andCond, orCond)
            table.updateFile()

def call_DB(command):
    cmdWords = command.split(' ')
    if len(cmdWords)<2:
        print("WRONG COMMAND!")
    else:
        if cmdWords[1] == 'INSERT':
            insertRecord(cmdWords)
        elif cmdWords[1] == 'UPDATE':
            updateRecord(cmdWords)
        elif cmdWords[1] == 'DELETE':
            deleteRecord(cmdWords)
        elif cmdWords[1] == 'SELECT':
            selectRecord(cmdWords)
        else:
            print("WRONG COMMAND!")

def sign_up(name, nid, password, phone, email):
    u = User(name=name, nid=nid, password=password, phone=phone, email=email)
    users.append(u)
    for table in tableList:
        if table.name == 'User':
            table.insert([name, nid, password, phone, email])
            table.updateFile()
    print("SIGNED UP SUCCESSFULLY")

def sign_in(nid, password):
    flag = False
    for u in users:
        if u.nid == nid and u.password == password:
            flag = True
    if flag:
        print("SIGNED IN SUCCESSFULLY")
    else: 
        print("INCORRECT CREDENTIALS")

def open_account(nid, alias, password):
    acc = Account(alias=alias, nid=nid, password=password)
    for u in users:
        if u.nid==nid:
            u.accs.append(acc)
            for table in tableList:
                if table.name == 'Account':
                    table.insert([alias, nid, password])
                    table.updateFile()
    print("ACCOUNT OPENED SUCCESSFULLY")

def account_report(nid):
    for u in users:
        if u.nid==nid:
            for acc in u.accs:
                print(f"ACCOUNT ALIAS: {acc.alias} ----- ACCOUNT BALANCE: {acc.balance}")
                print("----------------------------------------")
                print("--------------TRANSACTIONS--------------")
                print("----------------------------------------")
                for trans in acc.transactions:
                    print(f"AMOUNT: {trans.amount} ----- TYPE: {trans.tType}")
                print('\n')

def pay_bill(nid, account_alias, amount):
    for u in users:
        if u.nid==nid:
            for acc in u.accs:
                if acc.alias == account_alias:
                    t = Transaction(amount=amount, tType="withdraw")
                    acc.transactions.append(t)
                    acc.balance = acc.balance-amount
                    for table in tableList:
                        if table.name == 'Transaction':
                            table.insert([amount, "withdraw", account_alias])
                            table.updateFile()
    print("BILL WAS PAID SUCCESSFULLY")

def money_transfer(nid, from_alias, to_alias, amount):
    for u in users:
        if u.nid==nid:
            for acc1 in u.accs:
                for acc2 in u.accs:
                    if acc1.alias == from_alias and acc2.alias == to_alias:
                        acc1.balance = acc1.balance-amount
                        acc2.balance=acc2.balance+amount
                        acc1.transactions.append(Transaction(amount, "withdraw"))
                        acc2.transactions.append(Transaction(amount, "deposit"))
                        for table in tableList:
                            if table.name == 'Transaction':
                                table.insert([amount, "withdraw", from_alias])
                                table.updateFile()
                                table.insert([amount, "deposit", to_alias])
                                table.updateFile()
    print("MONEY TRANSFERRED SUCCESFULLY")

def add_star_account(nid, alias):
    for u in users:
        if u.nid==nid:
            for acc in u.accs:
                if acc.alias == alias:
                    u.stars.append(acc)
    print("STAR ACCOUNT ADDED SUCCESSFULLY")

def close_account(nid, alias, password):
    for u in users:
        if u.nid==nid:
            for acc in u.accs:
                if acc.alias == alias:
                    if acc.password != password:
                        print("WRONG PASSWORD!")
                    else:
                        if acc.balance != 0:
                            subs = input("Balance is more than 0, please insert a substitute account alias:")
                            money_transfer(nid=nid, from_alias=acc.alias, to_alias=subs, amount=acc.balance)
                        u.accs.remove(acc)
                        for t in tableList:
                            if t.name == 'Account':
                                conditions = [f"nid=={nid}", f"alias=={alias}"]
                                t.delete(conditions, True, False)
                                t.updateFile()
    print("ACCOUNT CLOSED SUCCESSFULLY")

def deposit(nid, alias, amount):
    for u in users:
        if u.nid==nid:
            for acc in u.accs:
                if acc.alias == alias:
                    acc.transactions.append(Transaction(amount=amount, tType="deposit"))
                    acc.balance = acc.balance+amount
                    for table in tableList:
                        if table.name == 'Transaction':
                            table.insert([amount, "deposit", alias])
                            table.updateFile()
    print("DEPOSITED SUCCESSFULLY")


def loan_request(nid, alias, amount):
    for u in users:
        if u.nid==nid:
            for acc in u.accs:
                if acc.alias == alias:
                    acc.transactions.append(Transaction(amount=amount, tType="deposit"))
                    acc.balance = acc.balance+amount
                    for table in tableList:
                        if table.name == 'Transaction':
                            table.insert([amount, "deposit", alias])
                            table.updateFile()
    
                    for i in range(12):
                        acc.transactions.append(Transaction(amount=amount/12, tType="withdraw"))
                        acc.balance = acc.balance-(amount/12)
                        for table in tableList:
                            if table.name == 'Transaction':
                                table.insert([amount/12, "withdraw", alias])
                                table.updateFile()
                        time.sleep(20)
    print("LOAN REQUEST WAS SUCCESSFUL")


def main():
    myFile = open('schema.txt', 'r')
    lines = myFile.readlines()

    count = 0
    t = None
    for line in lines:
        if line == '\n':
            count = 0
        elif count == 0:
            t = Table(line.strip(), [])
            tableList.append(t)
            count = 1
        else:
            words = line.strip().split(' ')
            name = ''
            fieldType = ''
            isUnique = False
            if len(words) == 3:
                name = words[0]
                fieldType = words[2]
                isUnique = True
            else:
                name = words[0]
                fieldType = words[1]
            
            f = Field(name=name, fieldType=fieldType, isUnique=isUnique)
            t.fields.append(f) 

    for tbl in tableList:
        tbl.updateFile()

    while(True):
        command = input()
        if command == 'quit':
            break
        if command[0] == '$':
            call_DB(command)
        else:
            if command == 'SIGN UP':
                name = input("Please insert your name:")
                nid = input("Please insert your National ID number:")
                password = input("Please insert your password:")
                phone = input("Please insert your phone:")
                email = input("Please insert your email:")
                sign_up(name, nid, password, phone, email)
            elif command == 'SIGN IN':
                nid = input("Please insert your National ID number:")
                password = input("Please insert your password:")
                sign_in(nid, password)
            elif command == 'OPEN ACCOUNT':
                nid = input("Please insert your National ID number:")
                alias = input("Please insert your account alias:")
                password = input("Please insert your account password:")
                open_account(nid, alias, password)
            elif command == 'ACCOUNT REPORT':
                nid = input("Please insert your National ID number:")
                account_report(nid)
            elif command == 'DEPOSIT':
                nid = input("Please insert your National ID number:")
                alias = input("Please insert your account alias:")
                amount = input("Please enter the amount:")
                deposit(nid, alias, amount)
            elif command == 'STARRED ACCOUNT':
                nid = input("Please insert your National ID number:")
                alias = input("Please insert your account alias:")
                add_star_account(nid, alias)
            elif command == 'MONEY TRANSFER':
                nid = input("Please insert your National ID number:")
                from_alias = input("From which account alias?")
                to_alias = input("To which account alias?")
                amount = input("Please enter the amount:")
                money_transfer(nid=nid, from_alias=from_alias, to_alias=to_alias, amount=amount)
            elif command == 'PAY BILL':
                nid = input("Please insert your National ID number:")
                bill_number = input("Please insert your bill number:")
                account_alias = input("Please insert your account alias:")
                amount = input("Please insert the amount:")
                pay_bill(nid, account_alias, amount)
            elif command == 'LOAN REQUEST':
                nid = input("Please insert your National ID number:")
                alias = input("Please insert your account alias:")
                amount = input("Please enter the amount:")
                loan_request(nid, alias, amount)
            elif command == 'CLOSE ACCOUNT':
                nid = input("Please insert your National ID number:")
                alias = input("Please insert your account alias:")
                password = input("Please insert your account password:")
                close_account(nid, alias, password)
            else:
                print('WRONG COMMAND!')
        

if __name__ == '__main__':
    main()