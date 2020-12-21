class objeto:
    def __init__(self,indice,valor,peso):
        self.__indice = indice
        self.__valor = valor
        self.__peso = peso
        self.__costo = valor/peso
    #Metodos get de la clase
    def getIndice(self):
        return self.__indice
    def getValor(self):
        return self.__valor
    def getPeso(self):
        return self.__peso
    def getCosto(self):
        return self.__costo

def ordenamiento(listaObjetos):
    resultado = listaObjetos
    resultado.sort(key=getCosto())
    return resultado

#Codigo de prueba del algoritmo
print("Hola soy un mensaje")
