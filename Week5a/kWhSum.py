# Copyright (C) Antti Ollila
# License: MIT

""" Tämä ohjelma laskee pyydetyn viikon sähkön kulutuksen ja tuotannon"""

from datetime import datetime, date, timedelta

while True:
    try:
        WeekInput = int(input("Anna viikkonumero (1–52): "))
        if 0 <= WeekInput <= 53:
            break   
        else:
            print("Viikkonumeron pitää olla 1–52")
    except ValueError:
        print("Anna kokonaisluku.")

def FileInit(File: str) -> list:
    """Pyytää tiedoston määrittelyyn ja alustaa listarakenteen"""
    Information = []
    with open(File, "r", encoding="utf-8") as f:
        next(f)
        for Line in f:
            Line = Line.strip()
            Fields = Line.split(';')
            #Fields = Fields[0].replace("T"," ")
            Information.append(DataType(Fields))
    return Information 

def DataType(Info: list)-> list:
    """Alustaa tietorakenteen"""
    InfoLine = []
    #Temp = 0 #datetime.strptime(str(Info[0]), "%Y-%m-%d").date()
    #Temp = Temp.date() #datetime.strptime(Info[0], "%Y-%m-%d")
    InfoLine.append(datetime.fromisoformat(Info[0]))
    for i in range(1,7):
        InfoLine.append(int(Info[i]))
    return InfoLine

def CountPhaseDay(DataIn: list) -> tuple:
    """Laskee vaiheen summan ensimmäisen rivin päivälle"""
    p = [0] * 7

    if not DataIn:
        return tuple(p)  # jos lista on tyhjä

    TargetDay = DataIn[0][0].date()

    for row in DataIn:
        if row[0].date() == TargetDay:
            for i in range(6):
                p[i] += row[i+1]
                p[6] += p[i]
    #print(TargetDay)
    return  tuple(p)

def Wday(dno: int) -> str:
    """Tuottaa viikonpäivän"""
    if dno == 1:
        DayName="Maanantai"
    elif dno == 2:
        DayName="Tiistai"
    elif dno == 3:
        DayName="Keskiviikko"
    elif dno == 4:
        DayName="Torstai"
    elif dno == 5:
        DayName="Perjantai"
    elif dno == 6:
        DayName="Lauantai"
    elif dno == 7:
        DayName="Sunnuntai"
    return DayName

####################################################

def InitialPrint():
    """Tulostaa otsikkopiirteet"""
    print()
    print(f"Viikon {WeekInput} sähkönkulutus ja -tuotanto (kWh, vaiheittain)")
    print("------------------------------------------------------")
    print("Päivä \t\t Pvm \t\tKulutus [kWh]                   Tuotanto [kWh] \t\t\tNetto")
    print("\t\t\t\tv1      v2      v3              v1     v2     v3")

#####################################################

def main():
    """Pääfunktio. Ajaa alafunktiot."""
    Numbers = FileInit(f"viikko{WeekInput}.csv")
    InitialPrint()
    #print(Numbers)
    Number=1
    for i in range(6):
        DayEle = CountPhaseDay(Numbers)
        DayName = Wday(Number)
        #print(DayEle)
        print(f"{DayName} \t paiva \t\t{DayEle[0]}\t{DayEle[1]}\t{DayEle[2]}\t\t{DayEle[3]}\t{DayEle[4]}\t{DayEle[5]}\t\t{DayEle[6]}")
        Number +=1
       
if __name__ == "__main__":
    main()