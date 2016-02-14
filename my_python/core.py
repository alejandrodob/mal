from _types import List

def _list(*args):
    return List(args)

def _count(expr):
    if expr == None:
        return 0
    return len(expr)

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
}
