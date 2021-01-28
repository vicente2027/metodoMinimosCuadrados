class Jacobi:
    def __init__(self):
        self.e1 = []
        self.e2 = []
        self.e3 = []

    def ingresar(self,h, c ):
        if h == 0:
            self.e1 = c
        elif h == 1:
            self.e2 = c
        else:
            self.e3 = c


    def despejar(self):
        e1_aux = self.e1
        self.e1[1] = e1_aux[1] * -1.0
j = Jacobi()


def main():

    print("Ingresa un sistema de ecuaciones equilibrado")
    dic = ("Ingresa el coeficiente de x", "Ingresa el coeficiente de y", "Ingresa el coeficiente de z", "= ")
    dic2 = (" de la primera ecuacion ", " de la segunda ecuacion ", " de la tercera ecuacion ", )
    for h in range(3):
        p = []
        for i in range(4):
            p.append(input(str(dic[i]) + str(dic2[h]) + "\n"))
        j.ingresar(h,p)
    j.despejar()
    print(j.e1)
    print(j.e2)
    print(j.e3)

main()