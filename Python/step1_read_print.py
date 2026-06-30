from printer import pr_str
from reader import read_str


def read_mal(string):
    return read_str(string)

def eval_mal(string):
    return string

def print_mal(string):
    return pr_str(string)

def rep_mal(string):
    return print_mal(eval_mal(read_mal(string)))


if __name__ == "__main__":
    while True:
        try:
            string_val = input('user> ')
        except EOFError:
            break

        print(rep_mal(string_val))

# python3 -m unittest -v
