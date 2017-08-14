#Programa para calcular los digitos de Pi
#Creado por @neriphy

from math import *
import webbrowser
from datetime import datetime

n = 2

respusta = 1

limite = int(input("Introduzca limite de suma: "))
instanteInicial = datetime.now()

while limite >= n:
	respusta = 1/(n**2) + respusta
	n = n + 1
	print(respusta)
	print (n)


respusta = sqrt(6*(respusta))

instanteFinal = datetime.now()
tiempo = instanteFinal - instanteInicial
segundos = tiempo.seconds
microsegundos = tiempo.microseconds
print(microsegundos,"microsegundos tardo en calcular o,", segundos,"segundos")


print("\nEl programa calculo que pi es aproximadamente:",respusta)

print("Si te ha servido este pequeño programa sigueme en Twitter")
webbrowser.open("https://twitter.com/neriphy")