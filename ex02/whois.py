import sys

arg = sys.argv
arg_count = len(sys.argv)
is_num = True
nb = 0

if arg_count > 1 :
    try :
        nb = int(arg[1])
    except :
        is_num = False
    if arg_count == 2 and is_num == True :
        if nb == 0 :
            print("I'm Zero.")
        elif nb % 2 == 0 :
           print("I'm Even.")
        else :
            print("I'm Odd.")
    else :
       print("ERROR")
