class Table:
    records = []
    def __init__(self, name: str, fields: list):
        self.name = name
        self.fields = fields

    def insert(self, fieldValues):
        print(fieldValues)
        self.records.append(fieldValues)

    def delete(self, record):
        pass

    def updateFile(self):
        maxLength = 0
        for field in self.fields:
            if len(field.name)>maxLength:
                maxLength = len(field.name)

        for r in self.records:
            for p in r:
                if len(r)> maxLength:
                    maxLength = len(r)        

        maxLength=maxLength+2
        lineLength = len(self.fields)*maxLength
        filename = self.name+'.txt'
        f = open(filename, "w")

        for i in range(lineLength):
            f.write("-")

        for field in self.fields:
            f.write(field.name)

        for rec in self.records:
            for part in rec:
                f.write(part)
                f.write("--")
            f.write("\n")    
        f.close()  


class Field:
    def __init__(self, name, fieldType, isUnique):
        self.name = name
        self.fieldType = fieldType
        self.isUnique = isUnique