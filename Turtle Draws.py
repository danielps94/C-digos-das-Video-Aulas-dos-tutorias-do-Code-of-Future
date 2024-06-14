# Vamos fazer alguns desenhos legais com o projeto Tartaruga.

#Importar o pacote Tartaruga
import turtle

# Vamos fazer uma boa configuração no turtle
turtle.bgcolor("black") # Cor de fundo
turtle.pensize(2) # Pen size
turtle.color("red")
turtle.speed(0)

# Desenhando um quadrado
#turtle.forward(180)  # Move forward
#turtle.left(90)     # Move 90 graus para a esquerda
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.done()  # habilita oturtle a ficar na tela


# Agora vamos fazer um projeto legal no Turtle
#for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
#    turtle.color(colours)
#   turtle.circle(150)
#    turtle.left(60)
#turtle.done()

# Vamos deixar isso mais legal
for i in range(6):
    for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(10)
turtle.done()