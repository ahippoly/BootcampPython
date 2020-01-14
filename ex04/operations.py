import sys

def print_usage() :
    print("Usage: python operations.py\nExample:\n\tpython operations.py 10 3")

arg = sys.argv
arg_count = len(arg)

if arg_count < 3 :
    print("InputError: 2 arguments required\n")
    print_usage()
elif arg_count >3 :
    print("InputError: too many arguments\n")
    print_usage()
else :
    try :
        nb1 = int(arg[1])
        nb2 = int(arg[2])
    except :
          nb1 = None
          nb2 = None  
    if not isinstance(nb1, int) or not isinstance(nb2, int) :
        print("InputError: only numbers\n")
        print_usage()
    else :
        print("Sum :       " + str(nb1 + nb2))
        print("Difference: " + str(nb1 - nb2))
        print("Product:    " + str(nb1 * nb2))
        if nb2 != 0 :
            print("Quotient:   " + str(nb1 / nb2))
            print("Remainder:  " + str(nb1 % nb2))
        else :
            print("Quotient:   ERROR (div by zero)")
            print("Remainder:  ERROR (modulo by zero)")
            
