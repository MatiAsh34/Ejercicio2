from ViajeroFrecuente import *
import csv

def menu():
	print ("----------Menu----------")
	print ("1- Consultar Cantidad de Millas")
	print ("2- Acumular Millas")
	print ("3- Canjear Millas")
	print ("4- Salir")

def opciones(viajero):
	codigo = None
	while codigo != 4:
		menu()
		codigo = int(input("Codigo: "))

		if codigo == 1:
			print(viajero.cantidadTotalMillas())

		elif codigo == 2:
			millas_recorridas = int(input("Ingrese millas recorridas: "))
			millas_acum = viajero.acumularMillas(millas_recorridas)
			print("Millas acumuladas: ",millas_acum)

		elif codigo == 3: 
			millas_canjear = int(input("Ingrese millas a canjear: "))
			millas_acum = viajero.canjearMillas(millas_canjear)
			print("Millas acumuladas: ",millas_acum)

		elif codigo == 4:
			print("Saliendo...")

def Busca_Viajero():
	codigo_viajero = int(input("Ingrese codigo de viajero frecuente: "))
	y=0
	indice = None

	while y<len(lista):
		if lista[y].get_numero_viajero() == codigo_viajero:
			indice = lista[y]
		y+=1
		
	if indice == None:
		print("Viajero no encontrado!")
	else:
		opciones(indice)

if __name__ == '__main__':
	archivo = open('DatosViajeros.csv')
	reader = csv.reader(archivo,delimiter=',')
	lista = []

	for fila in reader:
		Viajero = ViajeroFrecuente(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
		lista.append(Viajero)

	Busca_Viajero()