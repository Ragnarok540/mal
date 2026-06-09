require "./types"

def pr_str(mal)
    if mal.kind_of?(Array) then
        return pr_list(mal)
    end

    if mal.kind_of?(MalSymbol) then
        return mal.to_s
    end

    if mal.kind_of?(MalNumber) then
        return mal.to_s
    end
end

def pr_list(mal)
    res = mal.map {|x| pr_str(x)}
    return "(" + res.join(" ") + ")"
end
