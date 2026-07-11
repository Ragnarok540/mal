class Env():
    def __init__(self, outer=None, binds=None, exprs=None):
        self.outer = outer
        self.data = {}
        if binds:
            binds = [b.val for b in binds]
            binds_len = len(binds)
            if '&' in binds and '&' == binds[-2]:
                start = list(exprs[:binds_len - 2])
                start.append(list(exprs[binds.index('&'):]))
                exprs = start
                binds.remove('&')
            for k, v in zip(binds, exprs):
                self.set(k, v)

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
