class Env():
    def __init__(self, outer=None, binds=None, exprs=None):
        self.outer = outer
        self.data = {}
        if binds and exprs:
            for k, v in zip(binds, exprs):
                self.set(k.val, v)

    def set(self, key, value):
        self.data[key] = value
        return value

    def get(self, key):
        try:
            return self.data[key]
        except KeyError:
            if self.outer:
                return self.outer.get(key)
            return None
