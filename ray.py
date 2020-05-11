import sys


def open_file(filename):
    data = open(filename,"r").read()
    return data

def lex(file_contents):
    tokens_list = []
    token = ""
    string = ""
    state = 0
    file_contents = list(file_contents)
    for c in file_contents:
        token += c
        if token == " ":
            if state == 0:
                token = ""
            else:
                token = " "
        elif token == "\n":
            token = ""
        elif token == "PRINT":
            tokens_list.append(token)
            token = ""
        elif token == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                tokens_list.append("STRING:" + string + "\"")
                string = ""
                state = 0
                token = ""
        elif state == 1:
            string += token
            token = ""
    return tokens_list

def parse(tokens):
    i = 0
    while(i < len(tokens)):
        if tokens[i] + " " + tokens[i+1][:6] == "PRINT STRING":
            print(tokens[i+1][7:] )
            i = i + 2

def run():
    data = open_file(sys.argv[1])
    tokens = lex(data)
    parse(tokens)

if __name__ == "__main__":
    run()