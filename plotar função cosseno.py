import numpy as np
import matplotlib.pyplot as plt

# Definindo a função que queremos plotar
def funcao(x):
    return np.sin(x)

# Criando um conjunto de valores de x
x = np.linspace(0, 2*np.pi, 100)  # 100 pontos igualmente espaçados entre 0 e 2*pi

# Calculando os valores correspondentes de y
y = funcao(x)

# Plotando a função
plt.plot(x, y)
plt.title('Gráfico de y = sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()