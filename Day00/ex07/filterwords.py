import sys
import re

arg = sys.argv

def err() :
    print("ERROR")



if (len(arg) > 2) :
    max = None
    try :
        max = int(arg[2])
    except :
        err()
    try :
        int(arg[1])
        err()
    except :
        if max != None :
            words = re.findall("\w+", arg[1])
            list_len = len(words)
            while list_len > 0 :
            #print(words[list_len])
            #print(len(words[list_len]))
                list_len -= 1
                if len(words[list_len]) <= max :
                    print(len(words[list_len]) , max)
                    del words[list_len]

            print(words)
    
else :
    err()
