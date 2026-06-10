require "./reader"
require "./printer"
require "./types"

def read_mal(str)
    return read_str(str)
end

def eval_mal(str, env)
    if str.kind_of?(Array) then
        res = str.map {|x| eval_mal(x, env)}
        res2 = res[1..-1].map{|x| x.to_i}.reduce(res[0][1], res[0][0])
        return MalNumber.new(res2)
    end

    if str.kind_of?(MalSymbol) then
        return env[str.val.to_sym]
    end

    if str.kind_of?(MalNumber) then
        return str.val
    end
end

def print_mal(str)
    return pr_str(str)
end

def rep_mal(str)
    repl_env = {
        "+": [:+, 0],
        "-": [:-, 0],
        "*": [:*, 1],
        "/": [:/, 1]
    }
    return print_mal(eval_mal(read_mal(str), repl_env))
end

while true
    print "user> "
    str = gets

    if str == nil then
        break
    end

    puts rep_mal(str)
end
