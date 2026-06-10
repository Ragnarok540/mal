class MalType
    attr_accessor :val

    def initialize(val)
        self.val = val
    end

    def to_s
        "#{self.val}"
    end
end

class MalNil < MalType
    def initialize()
        self.val = nil
    end

    def to_s
        "nil"
    end
end

class MalBool < MalType
    attr_accessor :t, :f

    def initialize(val)
        self.t = true
        self.f = false
        self.val = val
    end
end

class MalString < MalType
end

class MalNumber < MalType
end

class MalSymbol < MalType
end

class MalArray < MalType
    attr_accessor :start, :end
end

class MalVector < MalArray
    def initialize(val)
        self.start = "["
        self.end = "]"
        self.val = val
    end
end
