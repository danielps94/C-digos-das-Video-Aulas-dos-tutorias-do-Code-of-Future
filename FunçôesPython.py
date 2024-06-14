#Funções em Python

#Assim como na matematica onde uma função recebe um argumento e produz um resultado,
#isso pode ser feito também em phyton!!

# De forma geral uma função em python é descrita como:
# def function_name(arguments):
# { linhas que informam a função  que serão as intruçoes para a produção do resultado final}
# Retorna resultado final

# Como exemplo vamos produzir uma funação que retorne x^2 + y^2
def funçaoquadratica  (x , y):
    result = x**2 + y**2
    return result


print(funçaoquadratica(10 , 5))

# Vamos fazer uma nova funçao
def nascimento(pais):
    return print("Eu nasci no " + pais)

nascimento("Brasil")



