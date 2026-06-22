from mal_types import MalNumber, MalSymbol

def pr_str(mal):
    match type(mal).__name__:
        case list.__name__:
            res = map(pr_str, mal)
            return '(' + ' '.join(res) + ')'
        case MalNumber.__name__:
            # return repr(mal)
            return str(mal.val)
        case MalSymbol.__name__:
            # return repr(mal)
            return str(mal.val)
