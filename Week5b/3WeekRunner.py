# Copyright (C) 11/2025 Antti Ollila
# License: MIT
""" Tämä ohjelma käy läpi kolmen viikon sähkötiedot ja tuottaa niistä raportin """

from datetime import datetime, date, timedelta
import kWhSum
import io
import sys

AskWeeks = []

""" Kysytään viikot """
while len(AskWeeks) < 3:
    try:
        WeekInput = int(input("Anna viikkonumero (1–52): "))
        if 1 <= WeekInput <= 52:
            AskWeeks.append(WeekInput)
        else:
            print("Viikkonumeron pitää olla 1–52")
    except ValueError:
        print("Luku!")

""" Kysytään tiedostotulostus """ 
while True:
    OutputType = input("Haluatko tiedot tiedostoon? Y/N ").strip().lower()
    if OutputType in ("y", "n"):
        print()
        break
    print("Uusintakierros")

""" Tulostekaappaus ja palautus merkkijonona"""
def capture_output(func, *args, **kwargs) -> str: 
    buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer
    try:
        func(*args, **kwargs)
    finally:
        sys.stdout = old_stdout
    return buffer.getvalue()

"""" Tiedostokirjoitus. HUOM! Tietoinen append. """
def write_to_file(filename: str, text: str): 
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text + "\n")

""" Pääohjelma """
def main():
    trig = datetime.now()
    Total = 0 
    if OutputType == "y":
        write_to_file("stats.txt",f" Tuloste luotu {trig}.")
        for week in AskWeeks:
            report = capture_output(kWhSum.main, week)
            write_to_file("stats.txt", report)
        write_to_file("stats.txt",f"Pyydetyt viikot tulostettu onnistuneesti.")
        print("Raportti kirjoitettu tiedostoon stats.txt")
        print()
    else:
        print("Kolmen pyydetyn viikon tulosteet")
        for week in AskWeeks:
            print(capture_output(kWhSum.main, week))

if __name__ == "__main__":
    main()