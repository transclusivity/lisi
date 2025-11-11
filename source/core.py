from copy import deepcopy
from util import *

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

def enter (core):
    core.history.append(core.cursor)
    core.cursor = core.context.pop()

def leave (core):
    if core.history:
        core.cursor = core.history.pop()
    else:
        exit()


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

