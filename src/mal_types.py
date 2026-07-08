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

class MalBool(MalSymbol):
    def __init__(self, val):
        super().__init__(bool(val))

    def __str__(self):
        return str(self.val).lower()

class MalError(MalType):
    pass

class MalContainer(MalType):
    def __init__(self):
        self.val = []

class MalVector(MalContainer):
    def __init__(self):
        super().__init__()

    def __iter__(self):
        return iter(self.val)

class MalHashMap(MalContainer):
    def __init__(self):
        super().__init__()

class MalNil(MalType):
    def __init__(self):
        self.val = None

    def __str__(self):
        return 'nil'

def as_pairs(iterable):
    """ k0, v0, k1, v1 ...  ->  (k0, v0), (k1, v1) ... """
    it = iter(iterable)
    return zip(it, it)
