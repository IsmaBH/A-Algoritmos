#Funcion que implementa la transformada discreta de Fourier (naive)
#Utilizaremos la biblioteca cmath que nos permite trabajar
#mas comodamente con los numeros complejos
import cmath as cm
def dft(datos):
    #Preconstruimos algunos terminos
    suma = []
    w = 2*cm.pi 
    k = len(datos) - 1
    #Empezamos con las iteraciones
    for i in range(len(datos)):
        r = (-1j)*(w*i*k)
        z = r/(len(datos))
        exponencial = cm.exp(z)
        v = datos[i]*exponencial
        suma.append(v)
    #Hacemos la suma
    resultado = sum(suma)
    #Retornamos el resultado
    return resultado

datos = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.1]
print(dft(datos))
