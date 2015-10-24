import re

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
    if token == '\'':
        reader.next()
        return ['quote', read_form(reader)]
    if token == '`':
        reader.next()
        return ['quasiquote', read_form(reader)]
    if token == '~':
        reader.next()
        return ['unquote', read_form(reader)]
    if token == '~@':
        reader.next()
        return ['splice-unquote', read_form(reader)]
    if token == '@':
        reader.next()
        return ['deref', read_form(reader)]
    return read_atom(reader)


def read_list(reader):
    the_list = []
    reader.next()
    token = reader.peek()
    while token != ')':
        if token == EOF: raise ParensMissmatch("Missing ')'")
        the_list.append(read_form(reader))
        token = reader.peek()
    reader.next()
    return the_list


def read_atom(reader):
    return reader.next()


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
