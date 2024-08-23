import matplotlib.pyplot as plt
import numpy as np

def funcao_quadratica():
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))

    x = np.linspace(-5, 5, 100)
    y = a * x**2 + b * x + c

    plt.plot(x, y)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.title("Gráfico da Função Quadrática")
    plt.xlabel("X")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()

def funcao_afim():
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))

    x = np.linspace(-5, 5, 100)
    y = a * x + b

    plt.plot(x, y)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.title("Gráfico da Função Afim")
    plt.xlabel("X")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()

    def funcao_modular():
        

funcao_quadratica()
