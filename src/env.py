from mal_types import MalList

class Env():
    def __init__(self, outer=None, binds=None, exprs=None):
        self.outer = outer
        self.data = {}
        if binds:
            binds = [b.val for b in binds]
            exprs_it = iter(exprs)
            for i, bind in enumerate(binds):
                if bind == '&':
                    ml = MalList()
                    ml.val = list(exprs_it)
                    self.data[binds[i + 1]] = ml
                    break
                self.data[bind] = next(exprs_it)

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
