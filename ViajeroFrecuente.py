class ViajeroFrecuente():
	def __init__(self, num, dni, nombre, apellido, millas):
		self.__num_viajero = num
		self.__dni = dni
		self.__nombre = nombre
		self.__apellido = apellido
		self.__millas_acum = millas

	def cantidadTotalMillas(self):
		return self.__millas_acum	

	def acumularMillas(self, millas_recorridas):
		self.__millas_acum += millas_recorridas
		return self.__millas_acum

	def canjearMillas(self, millas_canjear):
		if millas_canjear <= self.__millas_acum:
			self.__millas_acum = self.__millas_acum - millas_canjear
			return(self.__millas_acum)
		else:
			print("La cantidad a canjear es mayor a las acumuladas")

	def get_numero_viajero(self):
		return self.__num_viajero
		