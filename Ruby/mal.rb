require "./reader"
require "./printer"

def read_mal(str)
    return read_str(str)
end

def eval_mal(str)
    return str
end

def print_mal(str)
    return pr_str(str)
end

def rep_mal(str)
    return print_mal(eval_mal(read_mal(str)))
end

while true
    print "user> "
    str = gets

    if str == nil then
        break
    end

    puts rep_mal(str)
end
