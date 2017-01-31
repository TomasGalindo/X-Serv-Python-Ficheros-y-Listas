#! /usr/bin/python3
#Vamos a utilizar la forma utilizando la funcion find
fich = open("/etc/passwd")

lineas = fich.readlines()

for linea in lineas:
	pos1 = linea.find(":")
	pos2 = linea.rfind(":")
	print(linea[: pos1] + " " + linea[pos2+1 :-1]);

