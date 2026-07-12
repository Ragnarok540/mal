from printer import pr_str
from reader import read_str
from env import Env
from core import ns
from mal_types import MalSymbol, MalVector, MalHashMap, MalError, MalNil, MalList, as_pairs

envi = Env()

for key, value in ns.items():
    envi.set(key, value)

def read_mal(string):
    res = read_str(string)
    return res

def eval_mal(mal, env):
    debug = env.get('DEBUG-EVAL')
    if debug and str(debug) not in ['nil', 'false']:
        print(f'EVAL: {pr_str(mal)}')
    match type(mal).__name__:
        case MalSymbol.__name__:
            res = env.get(mal.val)
            if not res:
                raise SymbolNotFound(f'error: symbol "{mal.val}" not found')
            return res
        case MalVector.__name__:
            new_vector = MalVector()
            new_vector.val = [eval_mal(e, env) for e in mal.val]
            return new_vector
        case MalHashMap.__name__:
            new_hashmap = MalHashMap()
            new_hashmap.val = [eval_mal(e, env) for e in mal.val]
            return new_hashmap
        case MalList.__name__:
            if len(mal) == 0:
                return mal
            match str(mal[0]):
                case 'def!':
                    return env.set(mal[1].val, eval_mal(mal[2], env))
                case 'let*':
                    let_env = Env(outer=env)
                    for k, v in as_pairs(mal[1]):
                        let_env.set(k.val, eval_mal(v, let_env))
                    return eval_mal(mal[2], let_env)
                case 'if':
                    parameter = eval_mal(mal[1], env)
                    if str(parameter) not in ['nil', 'false']:
                        return eval_mal(mal[2], env)
                    try:
                        return eval_mal(mal[3], env)
                    except IndexError:
                        return MalNil()
                case 'fn*':
                    def fn(*args):
                        fn_env = Env(outer=env, binds=mal[1], exprs=list(args))
                        return eval_mal(mal[2], fn_env)
                    return fn
                case 'do':
                    args = mal[1:]
                    res = [eval_mal(a, env) for a in args]
                    return res[-1]
            f = eval_mal(mal[0], env)
            args = mal[1:]
            return f(*[eval_mal(a, env) for a in args])
        case _:
            return mal

def print_mal(string):
    return pr_str(string)

def rep_mal(string):
    try:
        return print_mal(eval_mal(read_mal(string), envi))
    except SymbolNotFound as snf:
        return print_mal(MalError(snf))

rep_mal("(def! not (fn* (a) (if a false true)))")

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
