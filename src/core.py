from mal_types import MalNumber, MalBool, MalNil

ns = {
    '+': lambda a, b: MalNumber(a.val + b.val),
    '-': lambda a, b: MalNumber(a.val - b.val),
    '*': lambda a, b: MalNumber(a.val * b.val),
    '/': lambda a, b: MalNumber(int(a.val / b.val)),
    '=': lambda a, b: MalBool(type(a) == type(b) and a.val == b.val),
    '<': lambda a, b: MalBool(type(a) == type(b) == type(MalNumber(0)) and a.val < b.val),
    '<=': lambda a, b: MalBool(type(a) == type(b) == type(MalNumber(0)) and a.val <= b.val),
    '>': lambda a, b: MalBool(type(a) == type(b) == type(MalNumber(0)) and a.val > b.val),
    '>=': lambda a, b: MalBool(type(a) == type(b) == type(MalNumber(0)) and a.val >= b.val),
    'nil': MalNil(),
}


# <, <=, >, and >=: treat the first two parameters as numbers and do the corresponding numeric comparison, returning either true or false.