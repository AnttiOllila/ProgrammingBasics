# Copyright (c) 12-2025 Antti Ollila   
# License MIT

import datetime, time, sys

def ReportType()->int:
    """Pyytää raporttityypin: 1 Päiväkohtainen, 2 Kuukausikohtainen, 3 Vuosikohtainen, 4 Lopeta ohjelma"""
    while True:
        try:
            Type = int(input("Haluatko tiedot\n1) Päivältä?\n2) Kuukaudelta?\n3) Vuodelta?\n4) Lopettaa ohjelman?\n"))
            if Type in (1,2,3,4):
                return Type
            else:
                print("Uusintakierros")
        except ValueError:
            print("LUKU!")
    
def ActionAfterReport()->int:
    """Pyytää toiminnon raporttiin: 1 Kirjoita olemassa olevaan, 2 Kirjoita uuteen, 3 Lopeta ohjelma"""
    while True:
        try:
            Action = int(input("Haluatko:\n1) Kirjoita raportti tiedostoon report.txt?\n2) Luoda uuden raporttitiedoston?\n3) Lopettaa ohjelman?\n"))
            if Action in (1,2,3):
                return Action
            else:
                print("Uusintakierros")
        except ValueError:
            print("LUKU!")
    
def Report(material: list)->str:
    """Käsittelee luettavan tiedon"""

def FileInit(File: str) -> list:
    """Pyytää tiedoston määrittelyyn ja alustaa listarakenteen"""
    Information = []
    with open(File, "r", encoding="utf-8") as f:
        next(f)
        for Line in f:
            Line = Line.strip()
            Fields = Line.split(';')
            Information.append(DataType(Fields))
    return Information 

def WriteToFile(filename: str, text: str):
    """" Tiedostokirjoitus. HUOM! Tietoinen append. """ 
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def SuomiTime():
    return

def main():
    print()
    print("Tervetuloa sähköstatistiikkaohjelmaan!")
    print()
    ReportType()
    print()
    ActionAfterReport()
    return
    
if __name__ == "__main__":
    main()