
# own modules / modulos que podemos crear
# thirdy party modules / modulos que podemos descargar desde internet
# python modules / modulos de python

import datetime

print(datetime.date.today())
print(datetime.timedelta(minutes=67))

from datetime import timedelta, date
print(timedelta(minutes=500), date.today())
print(date.today(), timedelta(minutes=1000))

import myMath
myMath.suma(52,53)
myMath.resta(498,69)

from myMath import suma, resta
suma(46,57)
resta(574,546)

from colorama import Fore, Style, init
init(convert=True)
print(Fore.RED + "hola mundo")
