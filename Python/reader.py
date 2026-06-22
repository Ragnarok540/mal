import re

from mal_types import MalNumber, MalSymbol

class Reader:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def next(self):
        token = self.tokens[self.position]
        self.position += 1
        return token

    def peek(self):
        return self.tokens[self.position]

def read_str(string):
    tokens = tokenize(string)
    reader = Reader(tokens)
    return read_form(reader)

def tokenize(string):
    reg_exp = r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}('"`,;)]*)"""
    pattern = re.compile(reg_exp)
    return pattern.findall(string)

def read_form(reader):
    token = reader.peek()

    if token is None:
        return "BIG ERROR"

    if is_list_start(token):
        return read_list(reader)

    return read_atom(reader)


def read_list(reader):
    token = reader.next()
    result = []

    while True:
        token = reader.peek()

        if token is None:
            print("unbalanced")
            break

        if is_list_end(token):
            reader.next()
            break

        result.append(read_form(reader))

    return result

def read_atom(reader):
    token = reader.next()

    if is_number(token):
        return MalNumber(token)

    return MalSymbol(token)

def is_string(token):
    reg_exp = r""""(?:(?:[^"\\]|\\.)*")?"""
    pattern = re.compile(reg_exp)
    return pattern.match(token) is not None

def is_number(token):
    reg_exp = r"""-?\d+"""
    pattern = re.compile(reg_exp)
    return pattern.match(token) is not None

def is_list_start(token):
    return token[0] == '('

def is_list_end(token):
    return token[0] == ')'
