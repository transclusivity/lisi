def jump (core):
    core.cursor = core.context.pop()

def jumpif (core):
    if core.context.pop():
        core.cursor = core.context.pop()

def lit (value):
    return lambda core: core.context.append(value)

def show (core):
    print (" ".join (map (str, core.context)))

def drop (core):
    core.context.pop()

def swap (core):
    core.context[-2], core.context[-1] = core.context[-1], core.context[-2]

def over (core):
    core.context.append(deepcopy(core.context[-2]))

def dup (core):
    core.context.append(deepcopy(core.context[-1]))

def rot (core):
    core.context.append(core.context.pop(-3))

def monadic (term):
    def impl (core):
        core.context.append (term (core.context.pop()))
    return impl

def dyadic (term):
    def impl (core):
        b, a = core.context.pop(), core.context.pop()
        core.context.append (term (a, b))
    return impl

@dyadic
def add (a, b):
    return a + b

@dyadic
def sub (a, b):
    return a - b

@dyadic
def greater (a, b):
    return a > b

@dyadic
def lesser (a, b):
    return a < b

@dyadic
def both (a, b):
    return a and b

@dyadic
def either (a, b):
    return a or b

@monadic
def negate (x):
    return not x

