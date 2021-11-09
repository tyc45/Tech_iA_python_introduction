from random import uniform

def add(a,b):
    return a+b


def divide(a,b):
    return a/b

def add_integer(a,b):
    if type(a)==int and type(b)==int:    
        return a+b
    else:
        raise(TypeError("Parameters should be integers"))

def alea_uniform(a,b):
    return uniform(a,b)

