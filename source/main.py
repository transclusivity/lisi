from sys import argv as arguments

def main ():
    match arguments:
        case [_, location]:
            reference (location)
        case [_]:
            dialogue ()
        case unknown:
            pass

if __name__ == "__main__":
    main()
