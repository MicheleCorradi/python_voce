import pyttsx3
import os
engine = pyttsx3.init()
pyttsx3.speak("Enter number to open application")
while True:
    print("Enter to open application\n")
    print("\n1.MICROSOFT WORD\t 2.MICROSOFT EXCEL \n\t\t 3.GOOGLE CHROME \n\t 4.MICROSOFT EDGE\t 5.NOTEPAD \n\n\t\t 0.FOR EXIT")

    p = input()
    p = p.upper()

    if ("DONT" in p) or ("DON'T" in p) or ("NOT" in p):
        pyttsx3.speak("Type Again")
        print(".")
        print(".")
        continue
    
    elif("3" in p):
        os.system("start chrome")
        pyttsx3.speak("You open google chrome")

    elif("4" in p):
        os.system("start msedge")
        pyttsx3.speak("You open microsoft edge")

    elif("5" in p):
        os.system("start notepad")
        pyttsx3.speak("You open notepad")

    elif("2" in p):
        os.system("start excel")
        pyttsx3.speak("You open microsoft excel")

    elif("1" in p):
        os.system("start winword")
        pyttsx3.speak("You open microsoft word")

    elif("0" in p):
        pyttsx3.speak("Exiting")
        break

    else:
        pyttsx3.speak(p)
        print("Is Invalid,Please Try Again")
        pyttsx3.speak("is Invalis,Please try again")