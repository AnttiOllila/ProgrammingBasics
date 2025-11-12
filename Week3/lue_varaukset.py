"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin käyttäen funkitoita.
Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19,95 €
Kokonaishinta: 39,9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""
from datetime import datetime

def hae_varausnumero(varaus):
    nro = varaus[0]
    print(f"Varausnumero: {nro}")
def hae_varaaja(varaus):
    nimi = varaus[1]
    print(f"Varaaja: {nimi}")
def hae_paiva(varaus):
    pva = varaus[2]
    print(f"Varauspäivä: {pva}")
def hae_aloitusaika(varaus):
    aika = varaus[3]
    print(f"Aloitusaika: {aika}")
def hae_tuntimaara(varaus):
    maara = varaus[4]
    print(f"Varausnumero: {maara}")
def hae_tuntihinta(varaus):
    hinta = varaus[5]
    print(f"Tuntihinta: {hinta}")
def hae_maksettu(varaus):
    maks = varaus[6]
    print(f"Varaus maksettu: {maks}")
def hae_kohde(varaus): 
    kohde = varaus[7]
    print(f"Varauskohde: {kohde}")
def hae_puhelin(varaus): 
    puh = varaus[8]
    print(f"Puhelinnumero: {puh}")
def hae_sahkoposti(varaus):
    sposti = varaus[9]
    print(f"Sähköposti: {sposti}")
def laske_kokonaishinta(varaus):
    yht = varaus[4]*varaus[5]
    print(f"Hinta yhteensä: {yht}")

#def tulosta_varaus(varaus)

def main():
    # Maaritellaan tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto, luetaan ja splitataan sisalto
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()
        varaus = varaus.split('|')

    # Toteuta loput funktio hae_varaaja(varaus) mukaisesti
    # Luotavat funktiota tekevat tietotyyppien muunnoksen
    # ja tulostavat esimerkkitulosteen mukaisesti

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

if __name__ == "__main__":
    main()