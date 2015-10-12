import sys

def READ(code):
    return code

def EVAL(code):
    return code

def PRINT(code):
    return code

def REP(code):
    return PRINT(EVAL(READ(code)))

def loop():
    while True:
        try:
            user_input = raw_input("user> ")
            print REP(user_input)
        except EOFError:
            print ""
            print "Bye!"
            sys.exit(0)

if __name__ == '__main__':
    loop()
