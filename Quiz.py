#Teste seus conhecimentos!!

# Questão 1 - Atribuição de variáveis
# Em python é muito mais simples atribuir variáveis
# Com isso facilita também fazer as 4 operaões

x = 112
y = 4

print(x + y)
print(x * y)
print(x - y)
print(x / y)

# Questão número 2 - Fazer uma lista de 0 a 100
# Contenha apenas números pares
# Note que tambem é bem simples se criar uma lista
# que obedece a um determinada regra

minha_lista = list(range(0, 101, 2)) # Criador lista
print(minha_lista)

print(minha_lista[0:10]) # Primeiros 10 elementos

print(len(minha_lista))

minha_lista.append(True)
print(minha_lista)

# Questão 3 usar if para descobrir se um número é
# divisível por 5

numero = 12365984
if numero % 5 == 0:
    print("O numero  é divisível por 5")
else:
    print("O numero nao é divisível por 5")

# Questão 4 - Usando o loop 'for' fazer python
# imprimir os numeros de 0 a cinco
for i in range(6):  # lembre da regra n-1
    print(i)

# Questão 5 - Desenhar um pentagono
import turtle

for i in range(5):   # O Pentagono tem 5 lados
   turtle.right(72)  # Angulo que produz o pentagono
   turtle.forward(100)
turtle.done()

# Questão 6 - Criar uma função que testa se tres numeros
# formam um triplo pitagórico

def pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

print(pythagorean_triple(3, 4, 5))   # é um pitagorico
print(pythagorean_triple(7, 5, 32))  # N é um pitagórico

# Questão 7 - Porque este codigo está errado.
# n = 5
# while n > 0
# n = n + 1
#   print(n)

# Criar duas listas de comprimento 5 e
# plota-las umas contra as outras usando matplotlib

import matplotlib.pyplot as plt # Importando os módulos relevantes

lista1 = [1, 6, 13, 16, 24]
lista2 = [3, 7, 17, 28, 30]
plt.plot(lista1, lista2, c="blue", linewidth=1, label="A line!",
         linestyle="dashed", marker='s', markerfacecolor="purple", markersize=2)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Python Plot of a line")
plt.legend()
plt.show()






