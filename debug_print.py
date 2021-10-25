import inspect

def debug_print(elem):
    info = ""
    info += inspect.currentframe().f_back.f_code.co_filename
    info += ":"
    info += str(inspect.currentframe().f_back.f_lineno)
    info += " "
    info += "(" + inspect.currentframe().f_back.f_code.co_name + ")"
    print(info, str(type(elem)) + ": \"" + str(elem) + "\"")
