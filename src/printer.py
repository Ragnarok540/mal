from mal_types import MalNumber, MalBool, MalString, MalSymbol, MalKeyword, MalVector, MalNil, MalHashMap, MalError, MalList

def escape(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

def pr_str(mal, print_readably=True):
    match type(mal).__name__:
        case MalList.__name__:
            return '(' + pr_list(mal, ' ', print_readably) + ')'
        case MalVector.__name__:
            return '[' + pr_list(mal, ' ', print_readably)  + ']'
        case MalHashMap.__name__:
            return '{' + pr_list(mal, ' ', print_readably)  + '}'
        case MalNumber.__name__:
            return str(mal.val)
        case MalBool.__name__:
            return str(mal)
        case MalString.__name__:
            if print_readably:
                # return '"' + escape(mal.val) + '"'
                return mal.val
            return mal.val
        case MalKeyword.__name__:
            return str(mal.val)
        case MalSymbol.__name__:
            return str(mal.val)
        case MalNil.__name__:
            return str(mal)
        case MalError.__name__:
            return str(mal.val)
        case 'function':
            return '#<function>'
        case _:
            return str(mal)

def pr_list(mal, separator, print_readably):
    return separator.join(pr_str(exp, print_readably) for exp in mal)
