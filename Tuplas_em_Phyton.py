# Tuplas em Python

# Convencionalmente Tuplas se parecem com isso,
Frutas = ("Maçãs", 4, "Bananas", 5, "Laranjas", 6)
print(type(Frutas))

Lista_de_Frutas = ["Maçãs", 4, "Bananas", 5, "Laranjas", 6]

# Podemos modificar elementos em uma lista
#  Não podemos modificar elementos em uma tupla.

Lista_de_Frutas[0] = "Cerejas"

print(Lista_de_Frutas)

# Podemos realizar operações semelhantes em Tuplas assim como nas listas

# Podemos fatiar Tuplas
print(Frutas[0:3])

# Recolocando elementos em uma tupla
print(Frutas[0])

# Concatenação de tuplas.
Frutas = Frutas[0:4] + ("Ameixas", 10)
print(Frutas)

# Tuplas com um elemento
x = (5,) #Notação para tupla de um elemento
print(type(x))

# Podemos encontrar o elementos  de uma tupla
print(len(Frutas))

#Criando uma tupla
another_tuple = tuple(("hello", 18, True))
print(type(another_tuple))

#Convertendo uma Tupla para uma lista e de volta para tupla.
Frutas = list(Frutas)
print(type(Frutas))
Frutas.append("Peras")
fruit = tuple(Frutas)
print(Frutas)

#Também podemos descompactar tuplas
Frutas = ("Maças", "Bananas", "Peras",  "laranjas", "Cerejas"  )
print(len(Frutas))
(one, *two, three, four) = Frutas
print(one)
print(two)
print(three)

# Incorporar loops nas tuplas
for i in range(len(Frutas)):
    print(Frutas[i])







