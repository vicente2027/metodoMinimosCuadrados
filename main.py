import matplotlib.pyplot as plt
import numpy as np
class MinimosCuadrados:

    def __init__(self):
        self.t = 0
        self.x = []
        self.x_sum = 0
        self.y = []
        self.y_sum = 0
        self.xy = []
        self.xy_sum = 0
        self.x2 = []
        self.x2_sum = 0
        self.m = 0
        self.b = 0
        self.y_ = 0

    def introducir_valor(self, var, valor):
        if var == 'x':
            self.x.append(valor)
            self.x2.append(int(valor)*int(valor))
        else:
            self.y.append(valor)

    def sum(self):
        for i in range(self.t):
            self.x_sum += int(self.x[i])
            self.y_sum += int(self.y[i])
            self.xy_sum += int(self.xy[i])
            self.x2_sum += int(self.x2[i])

    def mi(self):
        #Pendiente
        p1 = self.xy_sum - (self.x_sum * self.y_sum) / self.t
        print(p1)
        p2 = self.x2_sum - ((self.x_sum * self.x_sum) / self.t)
        print(p2)
        self.m = p1 / p2
        #Punto que corta el eje y
        b1 = int(self.y_sum) / int(self.t)
        b2 = self.m
        b3 = int(self.x_sum) / int(self.t)
        self.b = b1 - b2 * b3
        print("b = " + str(self.b))
        #Y
        y_tem = -1 * self.m
        self.y_ = self.b / y_tem
        print("y = " + str(self.y_))
        return p1 / p2

m = MinimosCuadrados()

def main():
    terminos = input("Ingresa el numero de terminos")
    m.t = int(terminos)
    for i in range(int(terminos)): # Guarda los valores de x
        inp = input(str("Ingresa el valor de X ") + str(i) + "\n")
        m.introducir_valor('x', inp)
    for i in range(int(terminos)):# Guarda los valores de y
        inp = input(str("Ingresa el valor de Y ") + str(i) + "\n")
        m.introducir_valor('y', inp)
    for i in range(int(terminos)):# Guarda los valores de xy
        m.xy.append(int(m.x[i])*int(m.y[i]))
    m.sum()
    print("x = " + str(m.x))
    print("y = " + str(m.y))
    print("x2 = " + str(m.x2))
    print("xy = " + str(m.xy))
    print("sum x = " + str(m.x_sum))
    print("sum y = " + str(m.y_sum))
    print("sum x2 = " + str(m.x2_sum))
    print("sum xy = " + str(m.xy_sum))
    print("m = " + str(m.mi()))
    #print(m.b())

    #graficando
    ''' x = m.y_
        y = m.b
        plt.plot(100, x, color="#86D2FF", linewidth=2.0, label="Índice de comportamiento violento del hombre")
        plt.plot(100, y, color="#FF87D3", linewidth=2.0, label="Índice de independencia de la mujer")
    
        plt.show()
    '''

    plt.plot(m.x, m.y, 'ro')
    plt.show()

    plt.plot([m.y_, m.b])
    plt.show()
main()