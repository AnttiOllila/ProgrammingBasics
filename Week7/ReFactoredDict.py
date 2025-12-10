# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.
# -Modified to dict 12/2025 AOl-
# Tämä on luettavampi itse määrittelyssä, mutta tuloskäsittelyssä ei ole suuresti eroa. Tuo sanamuotoinen määrittely on sinänsä selkeä, mutta pitkä luettava.

from datetime import datetime

def muunna_varaustiedot(varaus_lista: list) -> dict:
    return {
    "id": int(varaus_lista[0]),
    "nimi": str(varaus_lista[1]),
    "sahkoposti": str(varaus_lista[2]),
    "puhelin": str(varaus_lista[3]),
    "paiva": datetime.strptime(str(varaus_lista[4]), "%Y-%m-%d").date(),
    "kellonaika": datetime.strptime(str(varaus_lista[5]), "%H:%M").time(),
    "kesto": int(varaus_lista[6]),
    "hinta": float(varaus_lista[7]),
    "vahvistettu": bool(varaus_lista[8]=="True" or varaus_lista[8]=="true"),
    "kohde": str(varaus_lista[9]),
    "luotu": (varaus_lista[10]),
    "lemmikki": (varaus_lista[11])
}

def hae_varaukset(varaustiedosto: str) -> list[dict]:
    varaukset = []
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def vahvistetut(varaukset: list) -> bool:
    for varaus in varaukset:
        if varaus["vahvistettu"] == True:# or varaus["vahvistettu"] == "true"):
            print(f"- {varaus["nimi"]}, {varaus["kohde"]}, {varaus["paiva"].strftime('%d.%m.%Y')} klo {varaus["kellonaika"].strftime('%H.%M')}")
    print()

def pitkat(varaukset: list) -> bool:
    for varaus in varaukset:
        if(varaus["kesto"] >= 3):
            print(f"- {varaus["nimi"]}, {varaus["paiva"].strftime('%d.%m.%Y')} klo {varaus["kellonaika"].strftime('%H.%M')}, kesto {varaus["kesto"]} h, {varaus["kohde"]}. Mukana {varaus["lemmikki"]}.")
    print()

def status(varaukset: list) -> bool:
    for varaus in varaukset:
        if(varaus["vahvistettu"] == True):
            print(f"{varaus["id"]} → Vahvistettu")
        else:
            print(f"{varaus["id"]} → EI vahvistettu")
    print()

def lkm(varaukset: list) -> int:
    vahvistetutVaraukset = 0
    eiVahvistetutVaraukset = 0
    for varaus in varaukset:
        if(varaus["vahvistettu"]==True):
            vahvistetutVaraukset += 1
        else:
            eiVahvistetutVaraukset += 1
    print(f"- Vahvistettuja varauksia: {vahvistetutVaraukset} kpl\n- Ei-vahvistettuja varauksia: {eiVahvistetutVaraukset} kpl\n")

def kokonaistulot(varaukset: list) -> float:
    varaustenTulot = 0
    for varaus in varaukset:
        if(varaus["vahvistettu"]==True):
            varaustenTulot += varaus["kesto"]*varaus["hinta"]
    print("Vahvistettujen varausten kokonaistulot:", f"{varaustenTulot:.2f}".replace('.', ','), "€\n")

def main():
    varaukset = hae_varaukset("varaukset.txt")
    print("1) Vahvistetut varaukset")
    vahvistetut(varaukset)
    print("2) Pitkät varaukset (≥ 3 h)")
    pitkat(varaukset)
    print("3) Varausten vahvistusstatus")
    status(varaukset)
    print("4) Yhteenveto vahvistuksista")
    lkm(varaukset)
    print("5) Vahvistettujen varausten kokonaistulot")
    kokonaistulot(varaukset)

if __name__ == "__main__":
    main()