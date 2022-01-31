class Table:
    records = []
    def __init__(self, name: str, fields: list):
        self.name = name
        self.fields = fields

    def insert(self, fieldValues):
        self.records.append(fieldValues)

    def update(self, fieldValues, conditions, andCond, orCond):
        if andCond:
            fIndex = 0
            sIndex = 0
            if '==' in conditions[0]:
                if '==' in conditions[1]:
                    firstcommand = conditions[0].split('==')
                    secondcommand = conditions[1].split('==')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]==firstcommand[1] and self.records[j][sIndex]==secondcommand[1]:
                            self.records[j] = fieldValues

                else:
                    firstcommand = conditions[0].split('==')
                    secondcommand = conditions[1].split('!=')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]==firstcommand[1] and self.records[j][sIndex]!=secondcommand[1]:
                            self.records[j] = fieldValues
            else:
                if '==' in conditions[1]:
                    firstcommand = conditions[0].split('!=')
                    secondcommand = conditions[1].split('==')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]!=firstcommand[1] and self.records[j][sIndex]==secondcommand[1]:
                            self.records[j] = fieldValues
                else:
                    firstcommand = conditions[0].split('!=')
                    secondcommand = conditions[1].split('!=')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]!=firstcommand[1] and self.records[j][sIndex]!=secondcommand[1]:
                            self.records[j] = fieldValues
        elif orCond:
            fIndex = 0
            sIndex = 0
            if '==' in conditions[0]:
                if '==' in conditions[1]:
                    firstcommand = conditions[0].split('==')
                    secondcommand = conditions[1].split('==')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]==firstcommand[1] or self.records[j][sIndex]==secondcommand[1]:
                            self.records[j] = fieldValues
                else:
                    firstcommand = conditions[0].split('==')
                    secondcommand = conditions[1].split('!=')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]==firstcommand[1] or self.records[j][sIndex]!=secondcommand[1]:
                            self.records[j] = fieldValues
            else:
                if '==' in conditions[1]:
                    firstcommand = conditions[0].split('!=')
                    secondcommand = conditions[1].split('==')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]!=firstcommand[1] or self.records[j][sIndex]==secondcommand[1]:
                            self.records[j] = fieldValues
                else:
                    firstcommand = conditions[0].split('!=')
                    secondcommand = conditions[1].split('!=')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]!=firstcommand[1] or self.records[j][sIndex]!=secondcommand[1]:
                            self.records[j] = fieldValues
        else:
            fIndex = 0
            if "==" in conditions[0]:
                firstcommand = conditions[0].split('==')
                for i in range(len(self.fields)):
                    if self.fields[i].name == firstcommand[0]:
                        fIndex = i
                for j in range(len(self.records)):
                        if self.records[j][fIndex]==firstcommand[1]:
                            self.records[j] = fieldValues
            else:
                firstcommand = conditions[0].split('!=')
                for i in range(len(self.fields)):
                    if self.fields[i].name == firstcommand[0]:
                        fIndex = i
                for j in range(len(self.records)):
                        if self.records[j][fIndex]!=firstcommand[1]:
                            self.records[j] = fieldValues

    def delete(self, conditions, andCond, orCond):
        if andCond:
            fIndex = 0
            sIndex = 0
            if '==' in conditions[0]:
                if '==' in conditions[1]:
                    firstcommand = conditions[0].split('==')
                    secondcommand = conditions[1].split('==')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]==firstcommand[1] and self.records[j][sIndex]==secondcommand[1]:
                            self.records.pop(j)

                else:
                    firstcommand = conditions[0].split('==')
                    secondcommand = conditions[1].split('!=')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]==firstcommand[1] and self.records[j][sIndex]!=secondcommand[1]:
                            self.records.pop(j)
            else:
                if '==' in conditions[1]:
                    firstcommand = conditions[0].split('!=')
                    secondcommand = conditions[1].split('==')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]!=firstcommand[1] and self.records[j][sIndex]==secondcommand[1]:
                            self.records.pop(j)
                else:
                    firstcommand = conditions[0].split('!=')
                    secondcommand = conditions[1].split('!=')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]!=firstcommand[1] and self.records[j][sIndex]!=secondcommand[1]:
                            self.records.pop(j)
        elif orCond:
            fIndex = 0
            sIndex = 0
            if '==' in conditions[0]:
                if '==' in conditions[1]:
                    firstcommand = conditions[0].split('==')
                    secondcommand = conditions[1].split('==')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]==firstcommand[1] or self.records[j][sIndex]==secondcommand[1]:
                            self.records.pop(j)
                else:
                    firstcommand = conditions[0].split('==')
                    secondcommand = conditions[1].split('!=')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]==firstcommand[1] or self.records[j][sIndex]!=secondcommand[1]:
                            self.records.pop(j)
            else:
                if '==' in conditions[1]:
                    firstcommand = conditions[0].split('!=')
                    secondcommand = conditions[1].split('==')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]!=firstcommand[1] or self.records[j][sIndex]==secondcommand[1]:
                            self.records.pop(j)
                else:
                    firstcommand = conditions[0].split('!=')
                    secondcommand = conditions[1].split('!=')
                    for i in range(len(self.fields)):
                        if self.fields[i].name == firstcommand[0]:
                            fIndex = i
                        if self.fields[i].name == secondcommand[0]:
                            sIndex = i
                    for j in range(len(self.records)):
                        if self.records[j][fIndex]!=firstcommand[1] or self.records[j][sIndex]!=secondcommand[1]:
                            self.records.pop(j)
        else:
            fIndex = 0
            if "==" in conditions[0]:
                firstcommand = conditions[0].split('==')
                for i in range(len(self.fields)):
                    if self.fields[i].name == firstcommand[0]:
                        fIndex = i
                for j in range(len(self.records)):
                        if self.records[j][fIndex]==firstcommand[1]:
                            self.records.pop(j)
            else:
                firstcommand = conditions[0].split('!=')
                for i in range(len(self.fields)):
                    if self.fields[i].name == firstcommand[0]:
                        fIndex = i
                for j in range(len(self.records)):
                        if self.records[j][fIndex]!=firstcommand[1]:
                            self.records.pop(j)

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