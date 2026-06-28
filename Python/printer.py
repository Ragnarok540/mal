from mal_types import MalNumber, MalString, MalSymbol, MalError

def pr_str(mal):
    match type(mal).__name__:
        case list.__name__:
            res = map(pr_str, mal)
            return '(' + ' '.join(res) + ')'
        case MalNumber.__name__:
            return str(mal.val)
        case MalString.__name__:
            return str(mal.val)
        case MalSymbol.__name__:
            return str(mal.val)
        case MalError.__name__:
            return str(mal.val)
