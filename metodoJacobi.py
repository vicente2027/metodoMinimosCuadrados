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



j = Jacobi()


def main():


    dic = ("Ingresa el coeficiente de x", "Ingresa el coeficiente de y", "Ingresa el coeficiente de z", "= ")
    dic2 = (" de la primera ecuacion ", " segunda ecuacion ", " tercera ecuacion ", )
    for h in range(3):
        p = []
        for i in range(4):
            p.append(input(str(dic[i]) + str(dic2[h]) + "\n"))
        j.ingresar(h,p)
    

main()