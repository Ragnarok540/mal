class MalType
end

class MalNil < MalType
    attr_accessor :NIL

    def initialize()
        self.NIL = nil
    end
end

class MalBool < MalType
    attr_accessor :TRUE, :FALSE

    def initialize()
        self.TRUE = true
        self.FALSE = false
    end
end

class MalString < MalType
    attr_accessor :STR # val

    def initialize(str)
        self.STR = str
    end
end

class MalNumber < MalType
    attr_accessor :num

    def initialize(number)
        self.num = number
    end

    def to_s
        "#{num}"
    end

end

class MalSymbol < MalType
    attr_accessor :sym

    def initialize(symbol)
        self.sym = symbol
    end

    def to_s
        "#{sym}"
    end
end

class MalList < MalType
    attr_accessor :LIST

    def initialize()
        self.LIST = Array.new()
    end
end
