import sys, traceback
import reader
import printer

def READ(code):
    return reader.read_str(code)

def EVAL(code):
    return code

def PRINT(code):
    return printer.pr_str(code)

def REP(code):
    return PRINT(EVAL(READ(code)))

def loop():
    while True:
        try:
            user_input = raw_input("user> ")
            print REP(user_input)
        except EOFError:
            print "\nBye!"
            sys.exit(0)
        except Exception as e:
            print "".join(traceback.format_exception(*sys.exc_info()))

if __name__ == '__main__':
    loop()
