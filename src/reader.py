import re

from mal_types import MalNumber, MalBool, MalString, MalSymbol, MalKeyword, MalVector, MalHashMap, MalError, MalList

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
    try:
        return read_form(reader)
    except UnbalancedError:
        return MalError('error: unbalanced')

def tokenize(string):
    reg_exp = r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}('"`,;)]*)"""
    pattern = re.compile(reg_exp)
    return pattern.findall(string)

def read_form(reader):
    token = reader.peek()
    if token == '':
        return MalError('error: no input')
    if is_list_start(token):
        return read_list(reader)
    if is_vector_start(token):
        return read_vector(reader)
    if is_hashmap_start(token):
        return read_hashmap(reader)
    if is_comment(token):
        reader.next()
        read_form(reader)
    return read_atom(reader)


def read_list(reader):
    token = reader.next()
    result = MalList()
    while True:
        token = reader.peek()
        if is_list_end(token):
            reader.next()
            break
        result.val.append(read_form(reader))
    return result

def read_vector(reader):
    token = reader.next()
    result = MalVector()
    while True:
        token = reader.peek()
        if is_vector_end(token):
            reader.next()
            break
        result.val.append(read_form(reader))
    return result

def read_hashmap(reader):
    token = reader.next()
    result = MalHashMap()
    while True:
        token = reader.peek()
        if is_hashmap_end(token):
            reader.next()
            break
        result.val.append(read_form(reader))
    return result

def read_atom(reader):
    token = reader.next()
    if is_number(token):
        return MalNumber(token)
    if is_keyword(token):
        return MalKeyword(token)
    if token == 'true':
        return MalBool(True)
    if token == 'false':
        return MalBool(False)
    if is_string(token):
        if is_malformed_string(token):
            raise UnbalancedError()
        return MalString(token)
    if token[0] == '"':
        raise UnbalancedError()
    return MalSymbol(token)

def is_string(token):
    reg_exp = r""""(?:(?:[^"\\]|\\.)*")?"""
    pattern = re.compile(reg_exp)
    matches = pattern.findall(token)
    return len(matches) == 1

def is_malformed_string(token):
    return len(token) == 1 or token[-1] != '"'

def is_number(token):
    reg_exp = r"""-?\d+"""
    pattern = re.compile(reg_exp)
    return pattern.match(token) is not None

def is_keyword(token):
    return token[0] == ':'

def is_comment(token):
    return token[0] == ';'

def is_list_start(token):
    return token[0] == '('

def is_list_end(token):
    try:
        return token[0] == ')'
    except IndexError as ie:
        raise UnbalancedError() from ie

def is_vector_start(token):
    return token[0] == '['

def is_vector_end(token):
    try:
        return token[0] == ']'
    except IndexError as ie:
        raise UnbalancedError() from ie

def is_hashmap_start(token):
    return token[0] == '{'

def is_hashmap_end(token):
    try:
        return token[0] == '}'
    except IndexError as ie:
        raise UnbalancedError() from ie

class UnbalancedError(Exception):
    pass
