# Strings

# Nós já cobrimos strings , integradores , floats , booleanos e listas

# Integradores floats e booleanos são todos considerados como tipos de dados simples
# Ou seja eles não podem ser divididos!!

# Listas e strings são diferentes , eles são feitos de pedaços menores
# que podem ser quebrados, fragmentados.

# Já sabemos o que são strings
print("Hello world!")
print(type("Hello, world!!"))


# Operaçoes com strings
# Adição sinal concatenação

Greeting = " Hello"
Name = " Daniel"
print(Greeting + Name)

# operador * ( Estrela )
print(Name*3)
print(Greeting + Name*3)
print((Greeting + Name)*3)

# Operador indíce
Name = "Daniel"
print(Name[2])
print(Name[0] + Name[3] + Name[0] + Name[3])

#Cortando strings
print(Name[0:6])
print(Name[:2])
print(Name[2:])

#Maiúsculas e minúsculas
Name = "Ellie"
print(Name.lower())
print(Name.upper())

# Contar quantas vezes um caractere aparece em um string
print(Name.count("i"))

# Realocar caracteres específicos com os outros.
print(Name.replace("l","d"))
Name = "Ellie"
New_Name = Name.replace("l", "d")
print(New_Name)

# Achar o comprimento de uma string
Name = "Daniel"
print(len(Name))

# Formatar strings
# your_name = input("Your Name: ")
# hello = "Hello {}".format(your_name)
# print(hello)

# Cada letra em python é associado com um numero específico
print("orange" < "strawberry")
print(ord("o"))
print(chr(78))

#podemos realizar matematica com strings

# Operadores In e NOT ]
fruit = "banana"
print("a" in fruit)
print("s" not in fruit)

#incorporate a few things we´ve learn't so far
x = "hello"
y = ""
for character in x:
    y = y+  character.upper()
print(y)




