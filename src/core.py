from mal_types import MalNumber, MalBool, MalNil
from printer import pr_str

def prn(a):
    print(pr_str(a, print_readably=True))
    return MalNil()

ns = {
    '+': lambda a, b: MalNumber(a.val + b.val),
    '-': lambda a, b: MalNumber(a.val - b.val),
    '*': lambda a, b: MalNumber(a.val * b.val),
    '/': lambda a, b: MalNumber(int(a.val / b.val)),
    '=': lambda a, b: MalBool(type(a) == type(b) and a == b),
    '<': lambda a, b: MalBool(type(a) == type(b) == type(MalNumber(0)) and a.val < b.val),
    '<=': lambda a, b: MalBool(type(a) == type(b) == type(MalNumber(0)) and a.val <= b.val),
    '>': lambda a, b: MalBool(type(a) == type(b) == type(MalNumber(0)) and a.val > b.val),
    '>=': lambda a, b: MalBool(type(a) == type(b) == type(MalNumber(0)) and a.val >= b.val),
    'list': lambda *a: list(a),
    'list?': lambda a: MalBool(isinstance(a, list)),
    'empty?': lambda a: MalBool(a == []),
    'count': lambda a: MalNumber(len(a)) if isinstance(a, list) else MalNumber(0),
    'prn': prn,
    'nil': MalNil(),
}
