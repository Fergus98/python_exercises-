# return masked string
def maskify(cc):
    new_string = ''
    if len(cc) > 4:
        new_string += '#' * (len(cc) - 4) + cc[-4:]
        return new_string
    else:
        return cc
