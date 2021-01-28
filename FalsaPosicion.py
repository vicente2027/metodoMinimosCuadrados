class FalsaPosicion:

    def __init__(self):
        self.fx = []
        self.x = []
        self.fa = []
        self.fb = []
        self.tolerancia = 0
        self.intervalo = []
        self.cifras = 0

    def ingresar_fx(self, c ):
        self.fx = c # valores de fx

    def ingresar_t_c(self, i, c):
        if i == 0:
            self.tolerancia = c
        else:
            self.cifras = c
    def ingresar_intervalo(self, c):
        self.intervalo = c


f = FalsaPosicion()


def main():

    #print("Ingresa los valores de v1, v2 y v3 para la fucion f(x)= (v1)x^2 + (v2)x + (v3)")

    print("Fucion dada: f(x)= -(v1)x^2 + (v2)x + (v3)")
    dic = ("Ingresa el valor de v1", "Ingresa el valor de v2", "Ingresa el valor de v3")
    dic2 =("Ingresa la Tolerancia de error", "Ingresa las sifras significativas despues del 0")
    dic3 = ("Ingresa el primer Intervalo", "Ingresa el segundo Intervalo",)
    #dic2 = (" de la primera ecuacion ", " de la segunda ecuacion ", " de la tercera ecuacion ",)
    #for h in range(3):
    p = []
    for i in range(3): # f(x)
        p.append(input(str(dic[i]) + "\n"))
    f.ingresar_fx(p)
    print(f.fx)
    p.clear()
    for i in range(2): # intervalo
        p.append(input(str(dic3[i]) + "\n"))
    f.ingresar_intervalo(p)
    print(f.intervalo)
    aux = 0
    for i in range(2): # Tolerancia y Cifras
        aux = input(str(dic2[i]) + "\n")
        f.ingresar_t_c(i,aux)
    print(f.tolerancia)
    print(f.cifras)
main()

