from os import name, truncate
from database import Table, Field

def main():
    myFile = open('schema.txt', 'r')
    lines = myFile.readlines()
    tableList = []

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

    print(tableList)           



if __name__ == '__main__':
    main()