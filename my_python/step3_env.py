import sys, traceback
import reader
import printer
from _types import List, Symbol, Vector, Hash
from env import Env

repl_env = Env()
repl_env.set('+', lambda a,b: a+b)
repl_env.set('-', lambda a,b: a-b)
repl_env.set('*', lambda a,b: a*b)
repl_env.set('/', lambda a,b: int(a/b))


def READ(code):
    return reader.read_str(code)

def EVAL(ast, env):
    if type(ast) == List and len(ast) > 0:
        function = ast[0]
        if function == 'let*':
            scoped_env = Env(env)
            bindings = ast[1]
            for i in range(0, len(bindings), 2):
                symbol = Symbol(bindings[i])
                value = EVAL(bindings[i+1], scoped_env)
                scoped_env.set(symbol, value)
            expression = ast[-1]
            return EVAL(expression, scoped_env)
        elif function == 'def!':
            symbol = Symbol(ast[1])
            value = EVAL(ast[2], env)
            env.set(symbol, value)
            return value
        else:
            evaluated = eval_ast(ast, env)
            return evaluated[0](*evaluated[1:])
    evaluated = eval_ast(ast, env)
    return evaluated

def PRINT(code):
    return printer.pr_str(code)

def REP(code):
    return PRINT(EVAL(READ(code), repl_env))

def eval_ast(ast, env):
    if type(ast) == Symbol:
        return env.get(ast)
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
