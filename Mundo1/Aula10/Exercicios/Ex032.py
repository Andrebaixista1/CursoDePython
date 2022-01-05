# Ano é bixesto?
import datetime

anoBixesto = int(input("Digite um ano: "))

if anoBixesto == 0:
    anoBixesto = datetime.date.today().year
if anoBixesto % 4 == 0 and anoBixesto % 100 != 0 or anoBixesto % 400 == 0:
    print("O ano {} é bixesto".format(anoBixesto))
else:
    print("O ano {} não é bixesto".format(anoBixesto))