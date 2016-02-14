import re
from _types import List, Vector, Hash, Symbol, Integer, String, Keyword

EOF = None

class ParensMissmatch(Exception):
    pass

def read_str(string):
    tokens = tokenizer(string)
    reader = Reader(tokens)
    return read_form(reader)


def tokenizer(string):
    regexp = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"|;.*|[^\s\[\]{}()'"`@,;]+)""")
    return regexp.findall(string)


def read_form(reader):
    token = reader.peek()
    if token == '(':
        return read_list(reader)
    if token == ')':
        raise ParensMissmatch("Unexpected ')'")
    if token == '[':
        return read_vector(reader)
    if token == ']':
        raise ParensMissmatch("Unexpected ']'")
    if token == '{':
        return read_hash(reader)
    if token == '\'':
        reader.next()
        return List(['quote', read_form(reader)])
    if token == '`':
        reader.next()
        return List(['quasiquote', read_form(reader)])
    if token == '~':
        reader.next()
        return List(['unquote', read_form(reader)])
    if token == '~@':
        reader.next()
        return List(['splice-unquote', read_form(reader)])
    if token == '@':
        reader.next()
        return List(['deref', read_form(reader)])
    if token == '^':
        reader.next()
        meta = read_form(reader)
        return List(['with-meta', read_form(reader), meta])
    return read_atom(reader)


def read_list(reader):
    the_list = List()
    reader.next()
    token = reader.peek()
    while token != ')':
        if token == EOF: raise ParensMissmatch("Missing ')'")
        the_list.append(read_form(reader))
        token = reader.peek()
    reader.next()
    return the_list

def read_vector(reader):
    the_list = Vector()
    reader.next()
    token = reader.peek()
    while token != ']':
        if token == EOF: raise ParensMissmatch("Missing ']'")
        the_list.append(read_form(reader))
        token = reader.peek()
    reader.next()
    return the_list

def read_hash(reader):
    the_list = Hash()
    reader.next()
    token = reader.peek()
    while token != '}':
        if token == EOF: raise ParensMissmatch("Missing '}'")
        the_list.append(read_form(reader))
        token = reader.peek()
    reader.next()
    return the_list


def read_atom(reader):
    token = reader.next()
    if token[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return Integer(token)
    if token.startswith('"'):
        return String(token[1:-1].replace('\\"', '"'))
    if token.startswith(':'):
        return Keyword(token[1:])
    if token == 'true':
        return True
    if token == 'false':
        return False
    if token == 'nil':
        return None
    return Symbol(token)


class Reader(object):
    def __init__(self, tokens=[]):
        self.tokens = tokens
        self.pos = 0

    def next(self):
        token = self.peek()
        self.pos += 1
        return token

    def peek(self):
        if self.pos + 1 > len(self.tokens):
            return EOF
        return self.tokens[self.pos]
