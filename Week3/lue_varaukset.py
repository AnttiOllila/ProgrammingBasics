
from datetime import datetime

def hae_varausnumero(varaus):
    nro = int(varaus[0])
    print(f"Varausnumero: {nro}")
    return nro
def hae_varaaja(varaus):
    nimi = str(varaus[1])
    print(f"Varaaja: {nimi}")
    return nimi
def hae_paiva(varaus):
    pva = str(varaus[2])
    print(f"Varauspäivä: {pva}")
    return pva
def hae_aloitusaika(varaus):
    aika = str(varaus[3])
    print(f"Aloitusaika: {aika}")
    return aika
def hae_tuntimaara(varaus):
    maara = int(varaus[4])
    print(f"Varausnumero: {maara}")
    return maara
def hae_tuntihinta(varaus):
    hinta = float(varaus[5])
    print("Tuntihinta: ",f"{hinta:.2f}".replace('.',','), "€")
    return hinta
def hae_maksettu(varaus):
    maks = bool(varaus[6])
    print(f"Varaus maksettu: {maks}")
    return maks
def hae_kohde(varaus): 
    kohde = str(varaus[7])
    print(f"Varauskohde: {kohde}")
    return kohde
def hae_puhelin(varaus): 
    puh = int(varaus[8])
    print(f"Puhelinnumero: {puh}")
    return puh
def hae_sahkoposti(varaus):
    sposti = str(varaus[9])
    print(f"Sähköposti: {sposti}")
    return sposti
def laske_kokonaishinta(varaus):
    yht = float(varaus[4])*float(varaus[5])
    print(f"Hinta yhteensä: ",f"{yht:.2f}".replace('.',','), "€")
    return yht

def tulosta_varaus(varaus): 
    hae_varausnumero(varaus)
    hae_varaaja(varaus)
    hae_paiva(varaus)
    hae_aloitusaika(varaus)
    hae_tuntimaara(varaus)
    hae_tuntihinta(varaus)
    laske_kokonaishinta(varaus)
    hae_maksettu(varaus)
    hae_kohde(varaus)
    hae_puhelin(varaus)
    hae_sahkoposti(varaus)
    print()

def main():
    # Maaritellaan tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto, luetaan, splitataan ja tulostetaan sisalto
    with open(varaukset, "r", encoding="utf-8") as f:
        for line in f:
            varaus = line.strip()
            varaus = varaus.split('|')
            tulosta_varaus(varaus)

if __name__ == "__main__":
    main()