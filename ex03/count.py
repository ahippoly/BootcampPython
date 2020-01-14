import re

def text_analyzer(data = None) :
    """This fucking garbage function counts total character in the string and count various characters types """
    if data == None or not isinstance(data, str) :
        print("What is the text to analyse?")
        text = input()
    else :
        text = data

    char_count = len(text)
    upper_letters = len(re.findall("[A-Z]", text))
    lower_letters = len(re.findall("[a-z]", text))
    punct_mark = len(re.findall("[\.:;,\!\(\)\{\}\'\"\-]", text))
    spaces = len(re.findall(" ", text))
    print("The text contains " + str(char_count) + " characters:")
    print("- " + str(upper_letters) + " upper letters")
    print("- " + str(lower_letters) + " lower letters")
    print("- " + str(punct_mark) + " punctuation marks")
    print("- " + str(spaces) + " spaces")

