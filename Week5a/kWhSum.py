# Copyright (C) Antti Ollila
# License: MIT
""" Tämä ohjelma laskee pyydetyn viikon sähkön kulutuksen ja tuotannon"""

from datetime import datetime, date, timedelta

while True:
    try:
        print()
        WeekInput = int(input("Anna viikkonumero (1–52): "))
        if 0 <= WeekInput <= 53:
            break   
        else:
            print("Viikkonumeron pitää olla 1–52")
    except ValueError:
        print("Anna kokonaisluku.")
while True:
    try:
        OutputType = int(input("Annetaanko kulutus(1), tuotto(2) vai kaikki tieto(3)? "))
        if 0 <= OutputType <=4:
            break
        else:
            print("Valitse uudelleen ")
    except ValueError:
        print("Yritä edes ")

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

def DataType(Info: list)-> list:
    """Alustaa tietorakenteen"""
    InfoLine = []
    InfoLine.append(datetime.fromisoformat(Info[0]))
    for i in range(1,7):
        InfoLine.append(int(Info[i]))
    InfoLine.append(bool(False))
    return InfoLine

def CountPhaseDay(DataIn: list, target_day: date) -> tuple:
    """Laskee vaihesumman annetulle päivälle"""
    p = [0.0] * 7
    for row in DataIn:
        if row[0].date() == target_day:
            for i in range(6):
                p[i] += row[i+1] / 1000
    p[6] = sum(p[0:6])
    return tuple(p)

def Wday(dno: int) -> str: ### Kömpelö. En ole tyytyväinen.
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

def Cheapest(data: list, Temp:float) -> tuple:
    """Halvimman rivin tarkastus"""
    #if Temp <= 
    min_index = data + ("Ok",)#. min(range(len(data)), key=lambda i: data[i][6])
    return min_index

def InitialPrint(): ### Hiukan kömpelö suora printti.
    """Tulostaa otsikkopiirteet"""
    print()
    print(f"Viikon {WeekInput} sähkönkulutus ja -tuotanto (kWh, vaiheittain)")
    print("------------------------------------------------------")
    print("Päivä \t\t Pvm \t\tKulutus [kWh]                   Tuotanto [kWh] \t\t\tNettokulutus KWh")
    print("\t\t\t\t  v1 \t v2 \t v3 \t\t v1 \t v2 \t v3")

#####################################################

def main():
    """Pääfunktio. Ajaa alafunktiot."""
    Numbers = FileInit(f"viikko{WeekInput}.csv")
    InitialPrint()
    #print(Numbers)
    SDay = Numbers[0][0].date()
    CheapTemp=float()
    for i in range(7):
        TDay = SDay + timedelta(days=i)
        DayName = Wday(i+1)
        DayEle = CountPhaseDay(Numbers, TDay)
        DayEle = Cheapest(DayEle, CheapTemp)
        if OutputType == 1:
            ProdStr = f"{DayEle[0]:.2f}\t{DayEle[1]:.2f}\t{DayEle[2]:.2f}".replace(".",",")
        elif OutputType == 2:
            ProdStr = f"\t\t\t\t{DayEle[3]:.2f}\t{DayEle[4]:.2f}\t{DayEle[5]:.2f}".replace(".",",")
        else:
            ProdStr = f"{DayEle[0]:.2f}\t{DayEle[1]:.2f}\t{DayEle[2]:.2f}\t\t{DayEle[3]:.2f}\t{DayEle[4]:.2f}\t{DayEle[5]:.2f}\t\t{DayEle[6]:.2f}".replace(".",",")
        print(f"{DayName} \t {TDay.strftime("%d.%m.%Y")} \t {ProdStr}")
       
if __name__ == "__main__":
    main()