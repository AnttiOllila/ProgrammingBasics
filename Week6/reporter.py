# Copyright (c) 12-2025 Antti Ollila   
# License MIT

import sys
from datetime import datetime, date, timedelta
from zoneinfo import ZoneInfo
import calendar
counter=0

def ReportType()->int:
    """Pyytää raporttityypin: 1 Päiväkohtainen, 2 Kuukausikohtainen, 3 Vuosikohtainen, 4 Lopeta ohjelma"""
    while True:
        try:
            Type = int(input("Haluatko tiedot\n1) Päivältä?\n2) Kuukaudelta?\n3) Vuodelta?\n4) Lopettaa ohjelman?\n"))
            if Type in (1,2,3,4):
                if Type == 1:
                    TimeTemp=str(input("Anna päivä, jonka haluat raporttiin? pp.kk.vvvv "))
                    TDtemp  = datetime.strptime(TimeTemp, "%d.%m.%Y")
                    TDmax = TDtemp+timedelta(hours=23, minutes=59)
                elif Type==2:
                    TimeTemp=int(input("Anna kuukausi, jonka haluat raporttiin? kk "))
                    LastDay = calendar.monthrange(2025,TimeTemp)[1]
                    TDmax   = datetime(2025,TimeTemp,LastDay,23,59)
                    TimeTemp= f"01.{TimeTemp}.2025"
                    TDtemp  = datetime.strptime(TimeTemp, "%d.%m.%Y")  
                elif Type==3:
                    TDtemp  = datetime(2025,1,1,00,00)
                    TDmax = datetime(2025,12,31,23,59)
                else:
                    sys.exit(f"\nTulostettujen raporttien määrä: {counter}\nHyvää yötä!\n")
                return TDtemp, TDmax
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
                if Action == 3:
                    sys.exit(f"\nTulostettujen raporttien määrä: {counter}\nHyvää yötä!\n")
                else:
                    return Action
            else:
                print("Uusintakierros")
        except ValueError:
            print("LUKU!")
    
def Report(DataIn: list, StartDay: date, EndDay: date) -> tuple:
    """Käsittelee luettavan tiedon"""
    StartDay=StartDay.replace(tzinfo=ZoneInfo("Europe/Helsinki"))
    EndDay=EndDay.replace(tzinfo=ZoneInfo("Europe/Helsinki"))
    p = [0.0] * 8
    TempTemp = []
    for row in DataIn:
        if StartDay <= row[0] <= EndDay:
            p[0] += row[1]
            p[1] += row[2]
            TempTemp.append(row[3])
            if p[0]-p[1]>=p[4]:
                p[4]=p[0]-p[1]
                p[5]=row[3]
            if p[0]-p[1]<=p[6]:
                p[6]=p[0]-p[1]
                p[7]=row[3]    
    p[2] = p[0] - p[1]
    p[3] = sum(TempTemp) / len(TempTemp)
    print(p[4])                             # debug
    print(p[6])                             # debug
    return tuple(p)

def FileInit(File: str) -> list:
    """Pyytää tiedoston määrittelyyn ja alustaa listarakenteen"""
    Information = []
    with open(File, "r", encoding="utf-8") as f:
        next(f)
        for Line in f:
            Information.append(DataType(((Line.strip()).split(";"))))
    return Information 

def DataType(Info: list)-> list:
    """Alustaa tietorakenteen"""
    InfoLine = []
    InfoLine.append(datetime.fromisoformat(Info[0]))
    for i in range(1,4):
        InfoLine.append(float(str(Info[i]).replace(",",".")))
    return InfoLine

def WriteToFile(filename: str, text: str):
    """" Tiedostokirjoitus. HUOM! Tietoinen write. """ 
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text + "\n")

def FileName()->str:
    """Alustaa uuden tiedoston"""
    while True:
        try:
            NewName = str(input("Anna uusi tiedostonnimi: "))
        except ValueError:
            print("Kokeile uudestaan")
        NewName=f"{NewName}.txt"
        print(f"Uusi raporttitiedosto on {NewName}.txt")
        return NewName

def main():
    fileName="report.txt"
    print("\nTervetuloa sähköstatistiikkaohjelmaan!\n")
    DataMass=FileInit("2025.csv")
    days= ReportType()
    todo=ActionAfterReport()
    if todo == 2:
        fileName=FileName()
        days=ReportType()
    if todo == 1:
        Result=Report(DataMass,days[0],days[1])
        line = (f"\nHalutun aikavälin\t{days[0].strftime("%d/%m/%Y")} - {days[1].strftime("%d/%m/%Y")} tuloste:\n\nKulutettu energia:\t{Result[0]:.2f} kWh\nTuotettu energia:\t{Result[1]:.2f} kWh\nNettoenergia:\t\t{Result[2]:.2f} kWh\nKeskilämpötila:\t\t{Result[3]:.1f} 'C\n".replace(".",","))
        print(line)
        print({Result[4]})# f"{Result[5]}{Result[6]}{Result[7]}")                               #debug
        WriteToFile(fileName,line)
        global counter
        counter +=1
    return main()
    
if __name__ == "__main__":
    main()