# Copyright (c) 12-2025 co.op. Antti & Jussi Ollila 
# License MIT

import datetime, time, sys

MenuTree = {
    "main":{"title":"\nTervetuloa raportointiin\nHaluatko tiedot...", "sel":[
        ["Päivältä", "RepLength:1 NextMenu:day"],
        ["Kuukaudelta", "RepLenght:31 NextMenu:month"],
        ["Vuodelta", "RepLength:365 NextMenu:action"],
        ["Hei lopeta", "run:exit"],
    ]},
    "action":{"title":"\nHaluatko...", "sel":[
        ["Kirjoita report.txt", "run:WriteToFile"],
        ["Luo uusi tiedosto", "run:FileInit"],
        ["Salavalikkoon", "NextMenu:secret"],
        ["Päävalikkoon", "NextMenu:main"],
    ]},
    "secret":{"title":"\nSecret", "sel":[
        ["Hello World", "run:HelloWorld"],
        ["Päävalikkoon", "NextMenu:main"],
    ]},
    "day":{"title":"\nPäivä","sel":[
        []
    ]},
    "month":{"title":"\nKuukausi:", "sel":[
        ["Tammi", " NextMenu:action M:01"],["Helmi", "RepLenght:28 NextMenu:action M:02"],["Maalis", "NextMenu:action M:03"],["Huhti", "RepLenght:30 NextMenu:action M:04"],
        ["Touko", "NextMenu:action M:05"],["Kesä", "RepLenght:30 NextMenu:action M:06"],["Heinä", "NextMenu:action M:07"],["Elo", "NextMenu:action M:08"],
        ["Syys", "RepLenght:30 NextMenu:action M:09"],["Loka", "NextMenu:action M:10"],["Marras", "RepLenght:30 NextMenu:action M:11"],["Joulu", "NextMenu:action M:12"],
    ]}
}

opts = {
    "NextMenu":"main",
    "RepLength":"-1",
    "M":"01",
    "D":"01"
}

def HelloWorld():
    """Kicks"""
    print(f"Hello world! Opts:{opts}")

def WriteToFile():
    print(f"Wrote to file report of {opts["RepLength"]} days")

def FileInit()-> str:
    """File name changer"""
    while True:
        try:
            ReportFile=str(input("Anna uusi tiedostonnimi: "))
        except ValueError:
            print("Again")
        print(f"Uusi raporttitiedosto on {ReportFile}.txt")
        return ReportFile


def getInt(minVal, maxVal):
    """Menu change value"""
    while True:
        try:
            Choice = int(input("#"))
            if Choice < minVal:
                print(f"Vähintään {minVal}")
                continue
            if Choice > maxVal:
                print(f"Korkeintaan {maxVal}")
                continue
            return Choice
        except ValueError:
            print("Again")
            pass

def main():
    while True:
        CurrentMenu = MenuTree[opts["NextMenu"]]
        print(CurrentMenu["title"])
        for i, l in enumerate(CurrentMenu["sel"]):
            print(i + 1, l[0])
        choice = getInt(0 + 1, i + 1)
        cmds = CurrentMenu["sel"][choice-1][1]  #  Note indexing adjustment
        for cmd in cmds.split(" "):
            name, param = cmd.split(":")
            if name == "run":
                eval(param + "()")
            else:
                opts[name] = param
        print()
        print(choice)
    
if __name__ == "__main__":
    main()