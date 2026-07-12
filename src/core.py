from mal_types import MalNumber, MalString, MalBool, MalNil, MalList, MalContainer
from printer import pr_str

def fn_prn(a):
    print(pr_str(a, print_readably=True))
    return MalNil()

def fn_pr_str(*a):
    def pr_str_read(b):
        return pr_str(b, print_readably=True)
    res = map(pr_str_read, a)
    return MalString('"' + ' '.join(res) + '"')

def fn_str(*args):
    res = [pr_str(a) for a in args]
    if not res or res == ['']:
        return MalString('""')
    return MalString(''.join(res))

def fn_list(*a):
    ml = MalList()
    ml.val.extend(a)
    return ml

def fn_equals(a, b):
    if isinstance(a, MalContainer) and isinstance(b, MalContainer):
        return MalBool(a == b)
    if type(a) == type(b):
        return MalBool(a == b)
    return MalBool(False)

ns = {
    '+': lambda a, b: MalNumber(a.val + b.val),
    '-': lambda a, b: MalNumber(a.val - b.val),
    '*': lambda a, b: MalNumber(a.val * b.val),
    '/': lambda a, b: MalNumber(int(a.val / b.val)),
    '=': fn_equals,
    '<': lambda a, b: MalBool(type(a) == type(b) == type(MalNumber(0)) and a.val < b.val),
    '<=': lambda a, b: MalBool(type(a) == type(b) == type(MalNumber(0)) and a.val <= b.val),
    '>': lambda a, b: MalBool(type(a) == type(b) == type(MalNumber(0)) and a.val > b.val),
    '>=': lambda a, b: MalBool(type(a) == type(b) == type(MalNumber(0)) and a.val >= b.val),
    'list': fn_list,
    'list?': lambda a: MalBool(isinstance(a, MalList)),
    'empty?': lambda a: MalBool(len(a) == 0),
    'count': lambda a: MalNumber(len(a)) if isinstance(a, MalContainer) else MalNumber(0),
    'prn': fn_prn,
    'pr-str': fn_pr_str,
    'str': fn_str,
    'nil': MalNil(),
}
