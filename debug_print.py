import inspect

def debug_print(*argv):
    elem = ""
    for arg in argv:
        elem += str(type(arg)) + ": \"" + str(arg) + "\", "
    info = ""
    info += inspect.currentframe().f_back.f_code.co_filename
    info += ":"
    info += str(inspect.currentframe().f_back.f_lineno)
    info += " "
    info += "(" + inspect.currentframe().f_back.f_code.co_name + ")"
    print(info, elem)
