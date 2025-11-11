from dataclasses import dataclass, field

data = dataclass (slots = True)

def new (T):
    return field (default_factory=T)
