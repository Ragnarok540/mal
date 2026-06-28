class MalType():
    def __init__(self, val):
        self.val = val

class MalSymbol(MalType):
    pass

class MalString(MalSymbol):
    pass

class MalNumber(MalType):
    def __init__(self, val):
        super().__init__(int(val))

class MalError(MalType):
    pass
