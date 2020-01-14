import re, sys


morse		= { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----'}

arg = sys.argv

if len(arg) > 1 :
    arg.pop(0)
    text = " ".join(arg)
    text = text.upper()
    words = re.findall("\w+", text)
    err = 0
    for i in words :
        if not i.isalnum() :
            err = 1
    if err == 0 :
        morse_msg = []
        for word in words :
            morse_word = []
            for char in word :
                morse_word.append(morse[char])
                #print(char)
            morse_msg.append(" ".join(morse_word))
            #print(morse_word)
        
        print(" / ".join(morse_msg))
    else :
        print("ERROR")
