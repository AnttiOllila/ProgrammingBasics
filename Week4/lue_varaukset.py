"""
Ohjelma joka tulostaa tiedostosta luettujen varausten alkiot ja niiden tietotyypit

varausId | nimi | sähköposti | puhelin | varauksenPvm | varauksenKlo | varauksenKesto | hinta | varausVahvistettu | varattuTila | varausLuotu
------------------------------------------------------------------------
201 | Muumi Muumilaakso | muumi@valkoinenlaakso.org | 0509876543 | 2025-11-12 | 09:00 | 2 | 18.50 | True | Metsätila 1 | 2025-08-12 14:33:20
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
202 | Niiskuneiti Muumilaakso | niisku@muumiglam.fi | 0451122334 | 2025-12-01 | 11:30 | 1 | 12.00 | False | Kukkahuone | 2025-09-03 09:12:48
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
203 | Pikku Myy Myrsky | myy@pikkuraivo.net | 0415566778 | 2025-10-22 | 15:45 | 3 | 27.90 | True | Punainen Huone | 2025-07-29 18:05:11
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
204 | Nipsu Rahapulainen | nipsu@rahahuolet.me | 0442233445 | 2025-09-18 | 13:00 | 4 | 39.95 | False | Varastotila N | 2025-08-01 10:59:02
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
205 | Hemuli Kasvikerääjä | hemuli@kasvikeraily.club | 0463344556 | 2025-11-05 | 08:15 | 2 | 19.95 | True | Kasvitutkimuslabra | 2025-10-09 16:41:55
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
"""
from datetime import datetime, date, time

def muunna_varaustiedot(varaus: list) -> list:
    # Tähän tulee siis varaus oletustietotyypeillä (str)
    # Varauksessa on 11 saraketta -> Lista -> Alkiot 0-10
    # Muuta tietotyypit haluamallasi tavalla -> Seuraavassa esimerkki ensimmäisestä alkioista
    muutettuvaraus = []
    # Ensimmäisen alkion = varaus[0] muunnos
    muutettuvaraus.append(int(varaus[0]))
    # Ja tästä jatkuu
    muutettuvaraus.append(str(varaus[1]))
    muutettuvaraus.append(str(varaus[2]))
    muutettuvaraus.append(str(varaus[3]))
    pvm = datetime.strptime(str(varaus[4]), "%Y-%m-%d").date()
    muutettuvaraus.append(pvm)
    aika =datetime.strptime(str(varaus[5]), "%H:%M").time()
    muutettuvaraus.append(aika)
    muutettuvaraus.append(int(varaus[6]))
    muutettuvaraus.append(float(varaus[7]))
    maks = varaus[8].lower()== "true"  
    muutettuvaraus.append(maks)
    muutettuvaraus.append(str(varaus[9]))
    varaika = datetime.strptime(str(varaus[10]), "%Y-%m-%d %H:%M:%S")
    muutettuvaraus.append(varaika)
    return muutettuvaraus

def hae_varaukset(varaustiedosto: str) -> list:
    # HUOM! Tälle funktioille ei tarvitse tehdä mitään!
    # Jos muutat, kommentoi miksi muutit
    varaukset = []
    varaukset.append(["varausId", "nimi", "sähköposti", "puhelin", "varauksenPvm", "varauksenKlo", "varauksenKesto", "hinta", "varausVahvistettu", "varattuTila", "varausLuotu"])
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def main():
    # HUOM! seuraaville riveille ei tarvitse tehdä mitään!
    # Jos muutat, kommentoi miksi muutit
    # Kutsutaan funkioita hae_varaukset, joka palauttaa kaikki varaukset oikeilla tietotyypeillä
    varaukset = hae_varaukset("varaukset.txt")

    print()
    print('1) Vahvistetut varaukset')
    for varaus in varaukset[1:]:
        if (varaus[8] == True):
            pvm = datetime.strptime(str(varaus[4]), "%Y-%m-%d")
            pvm = pvm.strftime("%d-%m-%Y")
            print(f"{varaus[1]}, {varaus[8]}, {pvm}, klo {varaus[5]}")
    print()

    print('2 Pitkät varaukset (>= 3 h)')
    for varaus in varaukset[1:]:
        if (varaus[6] >= 3):
            pvm = datetime.strptime(str(varaus[4]), "%Y-%m-%d")
            pvm = pvm.strftime("%d-%m-%Y")
            print(f"{varaus[1]}, {pvm}, klo {varaus[5]}, {varaus[6]} h, {varaus[9]}")
    print()

    print('3 Varausten vahvistusstatus')
    for varaus in varaukset[1:]:
        if (varaus[8] == True):
            print(f"{varaus[1]} -> Vahvistettu ")
        else :
            print(f"{varaus[1]} -> Ei vahvistettu ")
    print()

    print('4 Yhteenveto vahvistuksista')
    yes=0
    no=0
    for varaus in varaukset[1:]: 
        if (varaus[8] == True):
            yes += 1
        else :
            no += 1
    print(f"- Vahvistettuja varauksia: {yes} kpl")
    print(f"- Vahvistamattomia varauksia: {no} kpl")
    print()

    print('5 Vahvistettujen varausten yhteissumma')
    money=float(0)
    for varaus in varaukset[1:]: 
        if (varaus[8] == True):
            money = money+(varaus[6]*varaus[7])
    strmoney=str(money).replace('.',',')
    print(f"Vahvistettujen varausten tulot: {strmoney} €")
    print()

 #   print('Kallein varaus:')
 #  Top=0.0
 #  for varaus in varaukset[1:]: 
 #       if (varaus[7] >= Top):
 #           Top = varaus[7]
 #           id = varaus  
 #   print(f"- Nimi: {id[1]}")
 #   print(f"- Varattu tila: {id[9]}")
 #   print(f"- Päivä: {id[4]}")
 #   print(f"- Aika: {id[5]}")
 #   print(f"- Kesto: {id[6]}")
 #   print(f"- Kokonaishinta: {Top}")

  #  print('Varausten määrä päivittäin')
  #  Sort= sorted(str(varaus), key=lambda rivi: rivi[4])
  #  for rivi in Sort:
  #      print(f"- {Sort[4]}: 1")
    #print(Sort)

if __name__ == "__main__":
    main()