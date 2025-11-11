from copy import deepcopy
from dataclasses import dataclass as data, field

def new (T):
    return field (default_factory=T)

@data
class Core:
    cursor  : int  = 0
    program : list = new (list)
    context : list = new (list)
    history : list = new (list)

def operate (core):
    while core.cursor < len (core.program):
        term = core.program [core.cursor]
        core.cursor += 1
        term (core)
    return core

def lit (value):
    return lambda core: core.context.append(value)

def enter (core):
    core.history.append(core.cursor)
    core.cursor = core.context.pop()

def leave (core):
    if core.history:
        core.cursor = core.history.pop()
    else:
        exit()

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

def main():
    core = Core()

    core.program.extend([
    	# prelude
        lit(16), enter, leave,  # call main, then exit
        lit(1),  add,   leave,  # increment word definition
        over,    over,  lesser, # equal word definition
        negate,  rot,   rot,
        greater, negate, both,
        leave,

        # main
        lit(15), lit(19),      # put 15 and 19 on the stack
        lit(3),  enter,        # call the increment word
        swap,    sub,          # swap the top two words and subtract them
        lit(5),  show,         # put the expected result on the stack and print the stack state
		lit(6),  enter, show,  # check for equality and show the result
        leave,                 # end main
    ])

    operate(core)

if __name__ == "__main__":
    main()

