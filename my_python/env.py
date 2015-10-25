from _types import Symbol

class Env(object):

    def __init__(self, outer=None):
        self.outer = outer
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def find(self, symbol):
        if symbol in self.data:
            return self
        return self.outer.find(symbol) if self.outer is not None else None

    def get(self, symbol):
        env = self.find(symbol)
        if env is None:
            raise Exception("Unable to resolve symbol '%s'" % symbol)
        value = env.data[symbol]
        return value
