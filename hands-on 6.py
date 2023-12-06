#K-Means
import matplotlib.pyplot as plt
import random
import math
import colorsys

class Dataset:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    

class Kmeans:
    def __init__(self, dataset, k ,iteraciones):
        self.dataset = dataset
        self.k = k
        self.iteraciones = iteraciones
        self.centroideX = []
        self.centroideY = []
        self.clases = []

    def clustering(self):
        #Sacamos k centroides en una coordenada aleatoria dentro del rango del dataset
        puntosAleatorios = list(range(len(self.dataset.getX())))
        random.shuffle(puntosAleatorios)

        for i in range(self.k):
            puntoAleatorio = puntosAleatorios.pop()
            centroideX = self.dataset.getX()[puntoAleatorio]
            centroideY = self.dataset.getY()[puntoAleatorio]
            self.centroideX.append(centroideX)
            self.centroideY.append(centroideY)
            self.clases.append(i)

        #Iteraciones a repetir todo el proceso de posicionamiento de los centroides
        for i in range(self.iteraciones):

            #Recorremos todo el dataset para asignar cada coordenada a un centroide más cercano (clase)
            clases = []
            for datasetX, datasetY in zip(self.dataset.getX(), self.dataset.getY()):
                distanciaCentroides = []

                #Sacamos distancia de una coordenada con cada centroide
                for centroideXAux, centroideYAux in zip(self.centroideX, self.centroideY):
                    distanciaX = (centroideXAux - datasetX) ** 2
                    distanciaY = (centroideYAux - datasetY) ** 2
                    distancia = math.sqrt(distanciaX + distanciaY)
                    distanciaCentroides.append(distancia)
                    
                #Le asignamos la clase del centroide más cercano
                posicion, distanciaMasCercana = min(enumerate(distanciaCentroides), key=lambda x: x[1])
                clase = self.clases[posicion]
                clases.append(clase)
            #plt.scatter(self.dataset.getX(), self.dataset.getY(), c=clases)
            #for centroideX, centroideY, clase in zip(self.centroideX, self.centroideY, self.clases):
                #plt.scatter(centroideX, centroideY, c="red", label='Centroide', marker='x', s=100)
            #plt.show()

            # Inicializar un diccionario para almacenar las posiciones de cada clase
            posicionesPorClase = {}

            # Iterar sobre las clases y almacenar las posiciones en el diccionario dependiendo la clase
            for posicion, clase in enumerate(clases):
                if clase not in posicionesPorClase:
                    posicionesPorClase[clase] = [posicion]
                else:
                    posicionesPorClase[clase].append(posicion)

            self.centroideX = []
            self.centroideY = []

            #Asignar los valores X Y de los centroides basándonos en su promedio
            for clase, posiciones in posicionesPorClase.items():
                valoresX = []
                valoresY = []
                for posicion in posiciones:
                    valoresX.append(self.dataset.getX()[posicion])
                    valoresY.append(self.dataset.getY()[posicion])

                promedioValoresX = sum(valoresX) / len(valoresX)
                promedioValoresY = sum(valoresY) / len(valoresY)
                self.centroideX.append(promedioValoresX)
                self.centroideY.append(promedioValoresY)
        #Fin de iteraciones

        #Recorremos todo el dataset para asignar cada coordenada a un centroide más cercano (clase)
        clases = []
        for datasetX, datasetY in zip(self.dataset.getX(), self.dataset.getY()):
            distanciaCentroides = []

            #Sacamos distancia de una coordenada con cada centroide
            for centroideXAux, centroideYAux in zip(self.centroideX, self.centroideY):
                distanciaX = (centroideXAux - datasetX) ** 2
                distanciaY = (centroideYAux - datasetY) ** 2
                distancia = math.sqrt(distanciaX + distanciaY)
                distanciaCentroides.append(distancia)

            #Le asignamos la clase del centroide más cercano
            posicion, distanciaMasCercana = min(enumerate(distanciaCentroides), key=lambda x: x[1])
            clase = self.clases[posicion]
            clases.append(clase)
                
        return clases, self.centroideX, self.centroideY, self.clases
    
    def generarColores(self, num_colores):
        colores = []
        for i in range(num_colores):
            hsv = (i / num_colores, 1.0, 1.0)
            rgb = colorsys.hsv_to_rgb(*hsv)
            colores.append(rgb)
        return colores


x =  [43, 35, 27, 41, 26, 3, 55, 28, 36, 59, 58, 14, 59, 59, 16, 4, 43, 18, 39, 47, 57, 22, 58, 70, 11, 68, 43, 31, 10, 35, 56, 37, 4, 9, 61, 35, 60, 27, 43, 11, 8, 50, 41, 45, 19, 8, 14, 35, 62, 20, 29, 32, 6, 39, 34, 52, 7, 66, 13, 26, 64, 2, 54, 20, 48, 40, 11, 69, 46, 56, 8, 31, 63, 66, 26, 53, 14, 50, 7, 48, 56, 33, 54, 12, 49, 63, 8, 28, 19, 69, 21, 46, 44, 32, 54, 36, 62, 54, 3, 51]
y =  [3, 13, 53, 65, 24, 68, 17, 25, 35, 42, 66, 67, 52, 65, 55, 49, 15, 31, 52, 27, 25, 60, 6, 14, 70, 22, 61, 43, 68, 65, 64, 55, 30, 28, 15, 53, 41, 20, 3, 63, 3, 10, 69, 1, 55, 66, 37, 31, 48, 51, 15, 57, 4, 10, 33, 26, 46, 63, 56, 70, 58, 69, 46, 28, 1, 19, 24, 54, 20, 63, 69, 69, 39, 68, 20, 9, 33, 54, 34, 10, 5, 30, 27, 17, 37, 33, 51, 1, 64, 60, 9, 18, 70, 28, 2, 3, 34, 63, 29, 60]
dataset = Dataset(x, y)

k = 10
iteraciones = 20
kmeans = Kmeans(dataset, k, iteraciones)
clases, centroidesX, centroidesY, todasLasClases = kmeans.clustering()

colores = kmeans.generarColores(max(todasLasClases) + 1)

plt.scatter(x, y, color=[colores[c] for c in clases])
for centroideX, centroideY, clase in zip(centroidesX, centroidesY, todasLasClases):
    plt.scatter(centroideX, centroideY, color=colores[clase], label='Centroide', marker='x', s=100)

plt.show()
