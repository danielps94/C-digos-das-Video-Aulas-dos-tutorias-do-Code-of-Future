# Media ponderada do CEFET

# Quantas provas voce fez
numero_de_provas = int(input("Entre com numero de provas realizadas: "))

# total de créditos que o exame cobre
total_creditos = int(input("Insira o total de creditos: "))

# começamos com a media zero para a seguir acrescentarmos os percentuais
average = 0
for exame in range(numero_de_provas):
    score = int(input("entre exame score: "))
    exame_creditos = int(input("Entre quantos creditos este exame cobre: "))
    average = average + score*exame_creditos/total_creditos
print("Sua media eh", average)
