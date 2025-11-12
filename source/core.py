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

