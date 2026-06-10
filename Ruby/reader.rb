require "./types"

class Reader
    attr_accessor :tokens, :position

    def initialize(tokens)
        self.tokens = tokens
        self.position = 0
    end

    def next
        token = self.tokens[self.position]
        self.position += 1
        return token
    end

    def peek
        return self.tokens[self.position]
    end
end

def read_str(str)
    tokens = tokenize(str)
    reader = Reader.new(tokens)
    return read_form(reader)
end

def tokenize(str)
    re = /[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}('"`,;)]*)/
    result = str.scan(re).flatten
    result.delete_at(-1)
    return result
end

def read_form(reader)
    token = reader.peek

    if token == nil then
        return "BIG ERROR"
    end

    if is_list_start(token) then
        return read_list(reader)
    end

    return read_atom(reader) 
end

def read_list(reader)
    token = reader.next
    result = Array.new()

    while true
        token = reader.peek

        if token == nil then
            print "unbalanced "
            break
        end

        if is_list_end(token) then
            reader.next
            break
        end

        result.push(read_form(reader))
    end

    return result
end

def read_atom(reader)
    token = reader.next

    if is_number(token) then
        return MalNumber.new(token)
    end

    return MalSymbol.new(token)
end

def is_string(token)
    re = /"(?:(?:[^"\\]|\\.)*")?/
    return token.match(re) != nil
end

def is_number(token)
    re = /-?\d+/
    return token.match(re) != nil
end

def is_list_start(token)
    return token[0, 1] == "("
end

def is_list_end(token)
    return token[0, 1] == ")"
end
