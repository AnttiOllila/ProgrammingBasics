"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""
#varaus = f.read().strip()
from datetime import datetime, timedelta, time

def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"
    TotalPrice=float(0)
    NotPaid=str('')
    Morning=str('')
    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        for line in f: 
            varaus = line.strip()

            varaus = varaus.split('|')

            varausnumero = int(varaus[0])
            varaaja = str(varaus[1])
            #aikakikkailut
            paiva = datetime.strptime(varaus[2], "%Y-%m-%d").date()
            suomalainenPaiva = paiva.strftime("%d.%m.%Y")
            aika = datetime.strptime(varaus[3], "%H:%M").time()
            suomalainenAika = aika.strftime("%H.%M")
            #määräsummakikkailut
            maara = int(varaus[4])
            hTemp = float(varaus[5])
            yhtTemp = maara*hTemp
            hinta = str(hTemp)
            hinta = hinta.replace('.',',')
            yht = str(yhtTemp)
            yht = yht.replace('.',',')
            #loppuaika
            EndDate = datetime.combine(paiva,aika)
            EndDate = EndDate + timedelta(hours=maara)
            finEndTime = EndDate.strftime("%d.%m.%Y %H.%M")

            maks = bool(varaus[6])
            kohde = str(varaus[7])
            puhno = str(varaus[8])
            sposti = str(varaus[9])

            #lisätehtävälaskuja
            TotalPrice = TotalPrice+yhtTemp
            if not maks:
                NotPaid = NotPaid+varaaja
            if aika >=time(8,0) and aika <=time(12,0): 
                Morning = Morning+' '+varaaja+','

    # Tulostetaan varaus konsoliin
            print(f"{varausnumero}\n{varaaja}\n{suomalainenPaiva}\n{suomalainenAika}\n{maara}\n{hinta}\n{yht}\n{maks}\n{kohde}\n{puhno}\n{sposti}")
            print('*')
            print(f"Varaus loppuu {finEndTime}")
            print()

    print('----------')
    print()
    print(f"Varauksien tuotto yhteensä: {TotalPrice}")
    print(f"Nämä eivät ole vielä maksaneet: {NotPaid}")
    print(f"Nämä alkavat aamupäivällä: {Morning}")

if __name__ == "__main__":
    main()