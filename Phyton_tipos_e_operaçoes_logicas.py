# Phyton types

# Tipos de dados básicos em Phyton
print(type("Ola mundo"))    # Dados tipo string
print(type(13))             # Dados tipo int
print(type(4.72))           # Dados tipo float
print(type(True))           # Dados tipo Booleano

# transformando float em inteiros
print(4.72, int(4.72)) #Phyton arredonda para baixo!
print(4.05, int(4.05))

# Arredondando para cima
print(4.72, int(4.72), int(round(4.72)))

# Transformando strings em inteiros
print("12345", int("12345"))

# Transformando em float
print(float(18))
print(float("12345"))

# Movendo para strings
print(str(18))
print(str(19.5))
print(type(str(19.5)))

# Operadores Lógicos
# Existem 3 tipos de operadores lógicos; 'and' 'or' 'not'

x = 6
print(x > 0 and x < 5)

y = 24
print(y % 2 == 0 or y % 5 == 0 )









