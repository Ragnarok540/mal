from mal_types import MalNumber, MalString, MalSymbol, MalKeyword, MalVector, MalNil, MalHashMap, MalError

def pr_str(mal):
    match type(mal).__name__:
        case list.__name__:
            res = map(pr_str, mal)
            return '(' + ' '.join(res) + ')'
        case MalVector.__name__:
            res = map(pr_str, mal.val)
            return '[' + ' '.join(res) + ']'
        case MalHashMap.__name__:
            res = map(pr_str, mal.val)
            return '{' + ' '.join(res) + '}'
        case MalNumber.__name__:
            return str(mal.val)
        case MalString.__name__:
            return str(mal.val)
        case MalKeyword.__name__:
            return str(mal.val)
        case MalSymbol.__name__:
            return str(mal.val)
        case MalNil.__name__:
            return str(mal)
        case MalError.__name__:
            return str(mal.val)
