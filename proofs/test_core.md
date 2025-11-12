```python
from source.core import *

core = Core()
```

```python
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
```

```python
operate(core)
```

