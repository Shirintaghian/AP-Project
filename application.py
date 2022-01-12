from database import Table, Field

tableList = []

def insertRecord(cmds):
    tableName = cmds[3]
    fields = cmds[5]
    fields.replace('(','')
    fields.replace(')','')
    fields.replace(';','')
    fieldValues = fields.split(',')

    for table in tableList:
        if table.name == tableName:
            if len(fieldValues) == len(table.fields):
                table.records.append(fieldValues)
                print(table.records)
            else:
                print("wrong number of fields")    

def updateRecord(cmds):
    pass

def deleteRecord(cmds):
    pass

def selectRecord(cmds):
    pass

def main():
    myFile = open('schema.txt', 'r')
    lines = myFile.readlines()

    count = 0
    t = None
    for line in lines:
        if line == '\n':
            count = 0
        elif count == 0:
            t = Table(line, [])
            tableList.append(t)
            count = 1
        else:
            words = line.split(' ')
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

    print("hello????")       
    while(True):
        command = input()
        if command == 'quit':
            break
        cmdWords = command.split(' ')
        if cmdWords[1] == 'INSERT':
            insertRecord(cmdWords)
        elif cmdWords[1] == 'UPDATE':
            updateRecord()
        elif cmdWords[1] == 'DELETE':
            deleteRecord()
        elif cmdWords[1] == 'SELECT':
            selectRecord()
        else:
            pass

if __name__ == '__main__':
    main()