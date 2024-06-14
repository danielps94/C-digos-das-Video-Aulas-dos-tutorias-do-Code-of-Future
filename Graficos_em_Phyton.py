#Importar os modulos relevantes
import matplotlib.pyplot as plt

# Gráficos em Phyton

# Grafico basico queremos algo melhor


#x = [1, 3, 5, 10]    # O que estamos plotando
#plt.plot(x)
# plt.show()             # Este comando mostra a plotagem desejada

#y = [7, 12, 21, 22]
#plt.plot(x, y)
# plt.show()

# Vamos plotar um gráfico bonitinho
x = [3, 9, 14]
y = [2, 7, 30]
# plotando x e y
plt.plot( x, y, c="red", linewidth=2, label="line 1")


# linha 2
x2 = [1, 15, 18]
y2 = [0, 3, 12]
# plotando x2 e y2
plt.plot( x2, y2, c="green", linewidth=2, label="line 1")

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Two lines!")

# mostrar legenda na plotagem
plt.legend()

# mostrar grafico
plt.show()




