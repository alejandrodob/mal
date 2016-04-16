from _types import List, String
from printer import pr_str

def _list(*args):
    return List(args)

def _count(expr):
    if expr == None:
        return 0
    return len(expr)

def _pr_str(*args):
    return String(" ".join(map(lambda exp: pr_str(exp, True), args)))

def _str(*args):
    return String("".join(map(lambda exp: pr_str(exp, False), args)))

def _prn(*args):
    print String(" ".join(map(lambda exp: pr_str(exp, True), args)))
    return None

def _println(*args):
    print String(" ".join(map(lambda exp: pr_str(exp, False), args)))
    return None

ns = {
    '+': lambda a,b: a+b,
    '-': lambda a,b: a-b,
    '*': lambda a,b: a*b,
    '/': lambda a,b: int(a/b),
    '<': lambda a,b: a<b,
    '<=': lambda a,b: a<=b,
    '>': lambda a,b: a>b,
    '>=': lambda a,b: a>=b,
    '=': lambda a,b: a==b,

    'list': _list,
    'list?': lambda a: type(a) == List,
    'empty?': lambda a: len(a) == 0,
    'count': _count,

    'pr-str': _pr_str,
    'str': _str,
    'prn': _prn,
    'println': _println,
}
