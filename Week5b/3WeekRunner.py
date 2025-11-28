# Copyright (C) Antti Ollila
# License: MIT
""" Tämä ohjelma käy läpi kolmen viikon sähkötiedot ja tuottaa niistä raportin"""

from datetime import datetime, date, timedelta
import sys

AskWeeks=[]
WantPrint=bool()

"""Kysymysalustus"""
while len(AskWeeks) <3:
    try:
        WeekInput = int(input("Anna viikkonumero (1–52): "))
        if 1 <= WeekInput <= 52:
            AskWeeks.append(WeekInput)  
        else:
            print("Viikkonumeron pitää olla 1–52")
    except ValueError:
        print("Anna kokonaisluku.")           
while True:
    try:
        OutputType = str(input("Haluatko tiedot tiedostoon? Y/N "))
        if OutputType == "Y" or OutputType == "y" :
            WantPrint=True
            break
        elif OutputType == "N" or OutputType == "n":
            WantPrint=False
            break
        else:
            print("Valitse uudelleen ")
    except ValueError:
        print("Yritä edes ")

def Write(File: str, info: str) -> str:
    with open(File, "w", encoding="utf-8") as f:
        print(info)
        sys.stdout = f
        #f.write(info)

import kWhSum ##Tuo alaohjelman

def main():
    """Pääohjelma"""
    if OutputType=="Y" or OutputType=="y":
        Write("stats.txt", kWhSum.main(AskWeeks[0]))    
        Write("stats.txt", kWhSum.main(AskWeeks[1])) 
        Write("stats.txt", kWhSum.main(AskWeeks[2]))
        sys.stdout = sys.__stdout__
    else:         
        kWhSum.main(AskWeeks[0])
        kWhSum.main(AskWeeks[1])
        kWhSum.main(AskWeeks[2])
if __name__ == "__main__":
    main()