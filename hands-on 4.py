class Dataset:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    

class SLR:
    def __init__(self, dataset):
        self.beta_0 = None
        self.beta_1 = None
        self.dataset = dataset

    def toComputeBeta0(self):
        n = len(self.dataset.getX())

        sumatoriaX = 0
        for valor in self.dataset.getX():
            sumatoriaX += valor

        sumatoriaY = 0
        for valor in self.dataset.getY():
            sumatoriaY += valor

        beta1 = self.beta_1

        beta0 = (sumatoriaY - (beta1 * sumatoriaX)) / n

        self.beta_0 = beta0

        return beta0
    
    def toComputeBeta1(self):
        n = len(self.dataset.getX())

        sumatoriaX = 0
        for valor in self.dataset.getX():
            sumatoriaX += valor

        sumatoriaY = 0
        for valor in self.dataset.getY():
            sumatoriaY += valor
            
        sumatoriaXY = 0
        for valorX, valorY in zip(self.dataset.getX(), self.dataset.getY()):
            valor = valorX * valorY
            sumatoriaXY += valor

        sumatoriaXcuadrada = 0
        for valorX in self.dataset.getX():
            valor = valorX * valorX
            sumatoriaXcuadrada += valor

        beta1 = ((n * sumatoriaXY) - (sumatoriaX * sumatoriaY)) / ((n * sumatoriaXcuadrada) - (sumatoriaX)**2)

        self.beta_1 = beta1

        return beta1
    
    def toPrintRegressionEq(self):
        print(f"y = {self.beta_0} + {self.beta_1}x")

    def toPredict(self, x):
        y = (self.beta_1 * x) + self.beta_0
        return y

#x = [23, 26, 30, 34, 43, 48, 52, 57, 58]
#y = [651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18]

dataset = Dataset(x, y)
slr = SLR(dataset)

slr.toComputeBeta1()
slr.toComputeBeta0()
slr.toPrintRegressionEq()

predecir = 40
print(f"La predicción de {predecir} es: {slr.toPredict(predecir)}")
predecir = 100
print(f"La predicción de {predecir} es: {slr.toPredict(predecir)}")
predecir = 67
print(f"La predicción de {predecir} es: {slr.toPredict(predecir)}")
predecir = 99
print(f"La predicción de {predecir} es: {slr.toPredict(predecir)}")
predecir = 23
print(f"La predicción de {predecir} es: {slr.toPredict(predecir)}")