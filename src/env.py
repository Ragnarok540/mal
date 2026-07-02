class Env():
    def __init__(self, outer=None):
        self.outer = outer
        self.data = {}

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
