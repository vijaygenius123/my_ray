import sys

def open_file(filename):
    data = open(filename,"r").read()
    print(data)

def run():
    data = open_file(sys.argv[1])

if __name__ == "__main__":
    run()