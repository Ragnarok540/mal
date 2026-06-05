function read_mal(str)
    return str
end

function eval_mal(str)
    return str
end

function print_mal(str)
    return str
end

function rep_mal(str)
    print_mal(eval_mal(read_mal(str)))
    return str
end

while true do
    io.write("user> ")
    str = io.read("*l")
    
    if str == nil then
        break
    end

    print(rep_mal(str))
end
