#KNN
import math
from collections import Counter
import matplotlib.pyplot as plt
import colorsys

class Dataset:
    def __init__(self, x, y, clases):
        self.x = x
        self.y = y
        self.clases = clases

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getClases(self):
        return self.clases
    
    def agregarPunto(self, x, y):
        self.x.append(x)
        self.y.append(y)

    def verPuntos(self):
        for x, y, clase in zip(self.x, self.y, self.clases):
            print("Coordenada (" + str(x) + ", " + str(y) + ") corresponde a la clase " + str(clase))
    

class KNN:
    def __init__(self, dataset, k):
        self.dataset = dataset
        self.k = k
        self.totalClases = None
        self.clases = None

    def sacarClases(self):
        clases = set(dataset.getClases())
        self.clases = list(clases)
        self.totalClases = len(self.clases)
    
    def obtenerClase(self, x, y):
        #Saca las distancias euclidianas de la coordenada proporcionada con todo el dataset
        distancias = []
        for puntoX, puntoY in zip(self.dataset.getX(), self.dataset.getY()):
            distanciaX = (puntoX - x) ** 2
            distanciaY = (puntoY - y) ** 2
            distancia = math.sqrt(distanciaX + distanciaY)
            distancias.append(distancia)

        #Se crea una lista de cada distancia que contiene en una tupla su distancia y su posición, se ordena para obtener los K más cercanos
        kMasCercanos = sorted(enumerate(distancias), key=lambda x: x[1])[:self.k]

        #Se separan las posiciones en una sola lista
        posicionesMasCercanas = []
        for posicion, valor in kMasCercanos:
            posicionesMasCercanas.append(posicion)

        #Se usan las posiciones para sacar las clases a las que corresponden
        clasesMasCercanas = []
        for posicion in posicionesMasCercanas:
            clasesMasCercanas.append(self.dataset.getClases()[posicion])

        #Se usa la funcion counter para obtener la clase más repetida en la lista
        contador = Counter(clasesMasCercanas)
        claseMasCercana, frecuencia = contador.most_common(1)[0]
        return claseMasCercana
    
    def agregarADataset(self, x, y):
        self.dataset.agregarPunto(x, y)

    def verDataset(self):
        self.dataset.verPuntos()

    def generarColores(self, num_colores):
        colores = []
        for i in range(num_colores):
            hsv = (i / num_colores, 1.0, 1.0)
            rgb = colorsys.hsv_to_rgb(*hsv)
            colores.append(rgb)
        return colores
    
    def getTotalClases(self):
        return self.totalClases, self.clases


x = [1, 9, 7, 3, -1, 2, 8, 5]
y = [1, 4, 5, 2, 0, 1, 7, 6]
clases = [1, 2, 2, 1, 1, 1, 2, 2]
k = 3

dataset = Dataset(x, y, clases)
knn = KNN(dataset, k)

knn.sacarClases()
totalClases, todasLasClases = knn.getTotalClases()

colores = knn.generarColores(totalClases + 1)

plt.scatter(x, y, color=[colores[todasLasClases.index(c)] for c in clases])

valorX = 9
valorY = 9
clase = knn.obtenerClase(valorX, valorY)

plt.scatter(valorX, valorY, color=colores[todasLasClases.index(clase)], marker='x', s=100)
print("Según las coordenandas proporcionadas (" + str(valorX) + ", " + str(valorY) + ") su clase es: " + str(clase))
plt.show()
