from mal_types import MalNumber, MalString, MalBool, MalNil, MalList, MalContainer
from printer import pr_str, pr_list
from reader import is_string

def fn_equals(a, b):
    if isinstance(a, MalContainer) and isinstance(b, MalContainer):
        return MalBool(a == b)
    if type(a) == type(b):
        return MalBool(a == b)
    return MalBool(False)

def fn_list(*a):
    ml = MalList()
    ml.val.extend(a)
    return ml

def fn_count(a):
    if isinstance(a, (MalContainer, list)):
        return MalNumber(len(a))
    return MalNumber(0)

def fn_prn(*args):
    print(pr_list(args, ' ', True))
    return MalNil()

def fn_println(*args):
    print(pr_list(args, ' ', False))
    return MalNil()

def fn_pr_str(*args):
    return pr_list(args, ' ', True)

def fn_str(*args):
    return pr_list(args, '', False)

ns = {
    '+': lambda a, b: MalNumber(a.val + b.val),
    '-': lambda a, b: MalNumber(a.val - b.val),
    '*': lambda a, b: MalNumber(a.val * b.val),
    '/': lambda a, b: MalNumber(int(a.val / b.val)),

    '=': fn_equals,
    '<': lambda a, b: MalBool(isinstance(a, MalNumber) and isinstance(b, MalNumber) and a.val < b.val),
    '<=': lambda a, b: MalBool(isinstance(a, MalNumber) and isinstance(b, MalNumber) and a.val <= b.val),
    '>': lambda a, b: MalBool(isinstance(a, MalNumber) and isinstance(b, MalNumber) and a.val > b.val),
    '>=': lambda a, b: MalBool(isinstance(a, MalNumber) and isinstance(b, MalNumber) and a.val >= b.val),

    'list': fn_list,
    'list?': lambda a: MalBool(isinstance(a, MalList)),
    'empty?': lambda a: MalBool(len(a) == 0),
    'count': fn_count,

    'prn': fn_prn,
    'println': fn_println,
    'pr-str': fn_pr_str,
    'str': fn_str,

    'nil': MalNil(),
}
