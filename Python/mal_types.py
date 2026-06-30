class MalType():
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

class MalSymbol(MalType):
    pass

class MalKeyword(MalSymbol):
    pass

class MalString(MalSymbol):
    pass

class MalNumber(MalType):
    def __init__(self, val):
        super().__init__(int(val))

class MalError(MalType):
    pass

class MalContainer(MalType):
    def __init__(self):
        self.val = []

class MalVector(MalContainer):
    def __init__(self):
        super().__init__()

class MalNil(MalType):
    def __init__(self):
        self.val = None

    def __str__(self):
        return 'nil'
