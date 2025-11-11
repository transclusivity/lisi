from util import *

@data
class Element:
    line     : int = 1 
    position : int = 1

    def __str__ (self):
        match self:
            case Blank ():
                return " " * self.width
            case Term ():
                if self.value [0].isdigit ():
                    return f"\x1b[36m{self.value}\x1b[0m"
                else:
                    return f"\x1b[35;3m{self.value}\x1b[0m"
            case Newline ():
                return f"\n{self.line + 1} | "

@data
class Blank (Element):
    width : int = 0

@data
class Newline (Element):
    pass

@data
class Term (Element):
    value : str = ""

@data
class Book:
    text     : list [str] = new (list)
    cursor   : int = 0 
    line     : int = 1 
    position : int = 1

    def __str__ (self):
        return f"{self.text[0].line} | " + "".join (map (str, self.text))

def analyze (source: str) -> Book:
    book = Book (); cursor = 0; line = 1; position = 1
    while cursor < len (source):
        match source [cursor]:
            case "(":
                while cursor < len (source) and source [cursor] != ")":
                    if whitespace == "\n":
                        cursor += 1; line += 1; position = 1
                    else:
                        cursor += 1; position += 1
                cursor += 1; position += 1
            case " " | "\t" as whitespace:
                blank = Blank (line, position)
                while cursor < len (source) and source [cursor] in " \t":
                    if whitespace == " ":
                        blank.width += 1
                    else:
                        blank.width += 4
                    cursor += 1; position += 1
                book.text.append (blank)
            case "\n":
                book.text.append (Newline (line, position))
                cursor += 1; line += 1; position = 1
            case symbol:
                term = Term (line, position)
                while cursor < len (source) and not (symbol := source [cursor]) in " \t\n(":
                    term.value += symbol
                    cursor += 1; position += 1
                book.text.append (term)
    return book

def read (book: Book):
    pass

