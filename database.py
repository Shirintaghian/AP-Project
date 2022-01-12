class Table:
    records = []
    def __init__(self, name: str, fields: list):
        self.name = name
        self.fields = fields

    def update(self, field):
        pass

    def delete(self, record):
        pass


class Field:
    def __init__(self, name, fieldType, isUnique):
        self.name = name
        self.fieldType = fieldType
        self.isUnique = isUnique