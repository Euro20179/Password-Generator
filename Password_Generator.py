import pyperclip
import string
import random

def inputs():
    while True:
        AVSU = (input("ascii or unicode (a/u): ")).lower()
        if AVSU == "a" or AVSU == "u": break 
        else:
            print("not a or u")
            continue

    while True:
        try: passLength = int(input("how many characters in password: ")); break
        except: print("NOT A NUMBER, PLS GIVE A NUMBER")
    return AVSU, passLength

def asciiPass(passLength):
    passWord = "".join([random.choice(string.printable) for x in range(passLength)])
    print(passWord, "\nit is now on your clipboard")
    pyperclip.copy(passWord)

def uniPass(passLength):
    passWord = "".join([chr(random.randint(0, 180000)) for x in range(passLength)])
    try: print(passWord)
    except: print("couldn't print password but it is on your clipboard")
    pyperclip.copy(passWord)

def main():
    cases = {"a": asciiPass, "u": uniPass}
    AVSU, passLength = inputs()
    cases[AVSU](passLength)
  
main()

while True:
    if (input("do you like your password (y/n): ")).lower() == "y": break
    else: main()