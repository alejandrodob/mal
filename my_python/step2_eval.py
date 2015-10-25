import sys, traceback
import reader
import printer
from _types import List, Symbol, Vector, Hash

repl_env = {
    '+': lambda a,b: a+b,
    '-': lambda a,b: a-b,
    '*': lambda a,b: a*b,
    '/': lambda a,b: int(a/b)
    }

def READ(code):
    return reader.read_str(code)

def EVAL(ast, env):
    evaluated = eval_ast(ast, env)
    if type(ast) == List:
        return evaluated[0](*evaluated[1:])
    return evaluated

def PRINT(code):
    return printer.pr_str(code)

def REP(code):
    return PRINT(EVAL(READ(code), repl_env))

def eval_ast(ast, env):
    if type(ast) == Symbol:
        return env[ast]
    elif type(ast) == List:
        return List([EVAL(elem, env) for elem in ast])
    elif type(ast) == Vector:
        return Vector([EVAL(elem, env) for elem in ast])
    elif type(ast) == Hash:
        return Hash([EVAL(elem, env) for elem in ast])
    else:
        return ast

def loop():
    while True:
        try:
            user_input = raw_input("user> ")
            print REP(user_input)
        except EOFError:
            print "\nBye!"
            sys.exit(0)
        except Exception as e:
            print "".join(traceback.format_exception(*sys.exc_info()))

if __name__ == '__main__':
    loop()
