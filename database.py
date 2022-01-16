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
                if len(p)> maxLength:
                    maxLength = len(p)        

        maxLength=maxLength+2
        lineLength = len(self.fields)*maxLength
        dashedLine = '-'*lineLength
        filename = self.name+'.txt'
        f = open(filename, "w")

        f.write(dashedLine)
        f.write("\n")

        for field in self.fields:
            f.write(field.name)
            f.write(' || ')
        f.write("\n")
        f.write(dashedLine)
        f.write("\n")

        for rec in self.records:
            for part in rec:
                f.write(part)
                f.write(" || ")
            f.write("\n") 
            f.write(dashedLine)
            f.write("\n")   
        f.close()  


class Field:
    def __init__(self, name, fieldType, isUnique):
        self.name = name
        self.fieldType = fieldType
        self.isUnique = isUnique