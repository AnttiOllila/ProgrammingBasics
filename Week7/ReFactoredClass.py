# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.
# -Modified to dict 12/2025 AOl-
# Tämä on luettavampi itse funktio- ja tulostekäsittelyssä.

from datetime import datetime

class Varaus:
    def __init__(self, uid=0, nimi="", sahkoposti="", puhelin="",paiva="", kellonaika="", kesto=0, hinta=0, vahvistettu="", kohde="", luotu="", lemmikki=""):
        self.id = uid
        self.nimi = nimi
        self.sahkoposti = sahkoposti
        self.puhelin = puhelin
        self.paiva = datetime.strptime(paiva, "%Y-%m-%d") if paiva else None
        self.kellonaika = datetime.strptime(kellonaika, "%H:%M") if kellonaika else None
        self.kesto = int(kesto)
        self.hinta = float(hinta)
        self.vahvistettu = str(vahvistettu).lower() == "true"
        self.kohde = kohde
        self.luotu = luotu
        self.lemmikki = lemmikki
    @property    
    def uid(self) -> int:
        return self.id
    def long(self) -> bool:
        return self.kesto >= 3
    def sum(self) -> float:
        return self.kesto * self.hinta
    def isok(self) -> bool:
        return self.vahvistettu
    def LePrint(self) -> str:
        print(f"- {self.nimi}, {(self.paiva).strftime('%d.%m.%Y')} klo {(self.kellonaika).strftime('%H.%M')}, kesto {self.kesto} h, {self.kohde}")
        return 

def hae_varaukset(varaustiedosto: str) -> list[Varaus]:
    varaukset = []
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split('|')
            varaukset.append(Varaus(*varaustiedot))#    muunna_varaustiedot(varaustiedot))
    return varaukset

def vahvistetut(varaukset: list):
    for varaus in varaukset:
        if varaus.isok():
            print(f"- {varaus.nimi}, {varaus.kohde}, {(varaus.paiva).strftime('%d.%m.%Y')} klo {(varaus.kellonaika).strftime('%H.%M')}. Mukana {varaus.lemmikki}.")
    print()

def pitkat(varaukset: list) -> bool:
    for varaus in varaukset:
        if varaus.long():
            Varaus.LePrint(varaus)#print(f"- {varaus.nimi}, {(varaus.paiva).strftime('%d.%m.%Y')} klo {(varaus.kellonaika).strftime('%H.%M')}, kesto {varaus.kesto} h, {varaus.kohde}")
    print()

def status(varaukset: list) -> bool:
    for varaus in varaukset:
        if varaus.isok():
            print(f"{varaus.uid} → Vahvistettu")
        else:
            print(f"{varaus.uid} → EI vahvistettu")
    print()

def lkm(varaukset: list) -> int:
    vahvistetutVaraukset = 0
    eiVahvistetutVaraukset = 0
    for varaus in varaukset:
        if varaus.isok():
            vahvistetutVaraukset += 1
        else:
            eiVahvistetutVaraukset += 1
    print(f"- Vahvistettuja varauksia: {vahvistetutVaraukset} kpl\n- Ei-vahvistettuja varauksia: {eiVahvistetutVaraukset} kpl\n")

def kokonaistulot(varaukset: list) -> float:
    varaustenTulot = 0
    for varaus in varaukset:
        if varaus.isok():
            varaustenTulot += varaus.sum()
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