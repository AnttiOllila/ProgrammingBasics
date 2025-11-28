import datetime
import locale

# 1
weekday_array = [
    "maanantai",
    "tiistai",
    "keskiviikko",
    "torstai",
    "perjantai",
    "lauantai",
    "sunnuntai"]

# 2
weekday_array = "maanantai tiistai keskiviikko torstai perjantai lauantai sunnuntai".split()

# 3
LOCALE = "fi_FI.UTF-8"
#LOCALE = fin_fin  # On windows locale name goes something like this

def weekday_names(locale_str):
    locale.setlocale(locale.LC_TIME, locale_str)
    names = []
    for day in range(7):
        names.append(datetime.datetime(2025, 1, 6 + day).strftime("%A"))
    return names

weekday_array = weekday_names(LOCALE)

# testprint
for d in weekday_array:
    print(d)
