from printer import pr_str
from reader import read_str
from mal_types import MalNumber, MalSymbol, MalVector, MalHashMap, MalNil, MalError, MalList

def read_mal(string):
    res = read_str(string)
    return res

def eval_mal(mal, repl_env):
    match type(mal).__name__:
        case MalSymbol.__name__:
            try:
                return repl_env[mal.val]
            except KeyError as ke:
                raise SymbolNotFound(f'error: symbol "{mal.val}" not found') from ke
        case MalVector.__name__:
            new_vector = MalVector()
            new_vector.val = [eval_mal(e, repl_env) for e in mal.val]
            return new_vector
        case MalHashMap.__name__:
            new_hashmap = MalHashMap()
            new_hashmap.val = [eval_mal(e, repl_env) for e in mal.val]
            return new_hashmap
        case MalList.__name__:
            if len(mal) == 0:
                return mal
            f = eval_mal(mal[0], repl_env)
            args = mal[1:]
            return f(*[eval_mal(a, repl_env) for a in args])
        case _:
            return mal

def print_mal(string):
    return pr_str(string)

def rep_mal(string):
    repl_env = {
        '+': lambda a, b: MalNumber(a.val + b.val),
        '-': lambda a, b: MalNumber(a.val - b.val),
        '*': lambda a, b: MalNumber(a.val * b.val),
        '/': lambda a, b: MalNumber(int(a.val / b.val)),
        'nil': MalNil(),
    }
    try:
        return print_mal(eval_mal(read_mal(string), repl_env))
    except SymbolNotFound as snf:
        return print_mal(MalError(snf))

class SymbolNotFound(Exception):
    pass

if __name__ == "__main__":
    while True:
        try:
            string_val = input('user> ')
        except EOFError:
            break
        print(rep_mal(string_val))

# python3 -m unittest -v
