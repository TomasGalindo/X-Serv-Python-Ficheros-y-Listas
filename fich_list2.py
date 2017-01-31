#! /usr/bin/python3

#Vamos a utilizar la forma utilizando la funcion split
fich = open("/etc/passwd")

lineas = fich.readlines()

for linea in lineas:
	palab_linea = linea.split(":")
	ident = palab_linea[0]
	shell = palab_linea[-1]
	print(ident + " " + shell[:-1])

