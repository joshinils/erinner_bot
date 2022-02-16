import inspect


def debug_print(*argv) -> None:  # type: ignore
    elem = ""
    for arg in argv:
        elem += str(type(arg)) + ": \"" + str(arg) + "\", "
    info = ""
    info += inspect.currentframe().f_back.f_code.co_filename  # type: ignore
    info += ":"
    info += str(inspect.currentframe().f_back.f_lineno)  # type: ignore
    info += " "
    info += "(" + inspect.currentframe().f_back.f_code.co_name + ")"  # type: ignore
    print(info, elem)
