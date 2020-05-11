import sys

def open_file(filename):
    data = open(filename,"r").read()
    return data

def lex(file_contents):
    token = ""
    string = ""
    state = 0
    file_contents = list(file_contents)
    for c in file_contents:
        token += c
        if token == " ":
            token = ""
        elif token == "PRINT":
            print("PRINT Command")
            token = ""
        elif token == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                print("String - ", string)
                string = ""
                state = 0
        elif state == 1:
            string += c
            tok = ""
    
    print(token)

def run():
    data = open_file(sys.argv[1])
    lex(data)

if __name__ == "__main__":
    run()