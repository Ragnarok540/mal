def read_mal(string):
    return string

def eval_mal(string):
    return string


def print_mal(string):
    return string


def rep_mal(string):
    return print_mal(eval_mal(read_mal(string)))


if __name__ == "__main__":
    while True:
        try:
            string = input('user> ')
        except EOFError:
            break

        print(rep_mal(string))

# python3 -m unittest 
