#Programa para calcular los digitos de Pi
#Creado por @neriphy

from math import *
import webbrowser

n = 2

respusta = 1

limite = int(input("Introduzca limite de suma: "))

while limite >= n:
	respusta = 1/(n**2) + respusta
	n = n + 1
	print(respusta)
	print (n)


respusta = sqrt(6*(respusta))


print("\nEl programa calculo que pi es aproximadamente:",respusta)

print("Si te ha servido este pequeño programa sigueme en Twitter")
webbrowser.open("https://twitter.com/neriphy")