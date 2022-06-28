def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    line = ("BestSchool, " * (magic_string.n - 1) + "BestSchool$")
    return line
