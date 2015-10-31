class Vector(list): pass

class List(list): pass

class Hash(list): pass

class Symbol(str): pass

class Integer(int): pass

class String(str): pass

class Keyword(str): pass

class Function(object):
    def __init__(self, env_class, bindings, outer_env, body, eval_func):
        def fn(*args):
            closure_env = env_class(outer=outer_env, binds=bindings, exprs=args)
            return eval_func(body, closure_env)
        self.fn = fn

    def __call__(self, *args):
        return self.fn(*args)
