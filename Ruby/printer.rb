require "./types"

def pr_str(mal)
    if mal.kind_of?(Array) then
        res = mal.each {|x| pr_str(x)}
        res2 = res.join(" ")
        return "(#{res2})"
    end

    if mal.kind_of?(MalSymbol) then
        return mal.to_s
    end

    if mal.kind_of?(MalNumber) then
        return mal.to_s
    end
end
