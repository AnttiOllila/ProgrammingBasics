# Copyright (c) 12-2025 Antti Ollila   
# License MIT

import datetime, time, sys

def MainMenu():
    while True:
        try:
            print("Päävalikko.")
            Choice = int(input("Haluatko käsitellä\n1) Vuositietoja\n2) Tarkemmin\n3) Lopettaa\n"))
            if Choice == 1:
                Sub1()
            elif Choice == 2:
                Sub2()
            elif Choice == 3:
                Sub2()
            else:
                print("Valitse uudelleen")
        except ValueError:
            print("LUKU!")
        return Choice
    
def Sub1():
    while True:
        try:
            print("Vuosivalikko")


def main():
    print()
    print("Tervetuloa sähköstatistiikkaohjelmaan!")
    print()
    MainMenu()
    print()
    #ActionAfterReport()
    return
    
if __name__ == "__main__":
    main()