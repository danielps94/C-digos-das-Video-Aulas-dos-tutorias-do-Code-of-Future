import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Configurações da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Corrida")

# Carregamento de imagens
carro_imagem = pygame.image.load('carro.png')
carro_imagem = pygame.transform.scale(carro_imagem, (50, 80))

cones_imagem = pygame.image.load('cones.png')
cones_imagem = pygame.transform.scale(cones_imagem, (50, 50))

fundo_imagem = pygame.image.load('fundo.jpg')
fundo_imagem = pygame.transform.scale(fundo_imagem, (largura, altura))

# Função para desenhar o carro
def desenhar_carro(x, y):
    tela.blit(carro_imagem, (x, y))

# Função para desenhar os cones
def desenhar_cones(lista_cones):
    for cones in lista_cones:
        tela.blit(cones_imagem, (cones[0], cones[1]))

# Função para criar novos cones
def criar_cones(lista_cones):
    x = random.randrange(0, largura - 50)
    y = random.randrange(-altura, -50)  # Colocar os cones acima da tela inicialmente
    lista_cones.append([x, y])

# Função para verificar colisões
def colisao(carro_x, carro_y, lista_cones):
    for cones in lista_cones:
        if carro_x + 50 > cones[0] and carro_x < cones[0] + 50:
            if carro_y < cones[1] + 50 and carro_y + 80 > cones[1]:
                return True
    return False

# Loop principal do jogo
def jogo():
    carro_x = largura // 2 - 25
    carro_y = altura - 100
    carro_velocidade = 0

    lista_cones = []
    for _ in range(3):  # Criar 3 cones inicialmente
        criar_cones(lista_cones)

    pontos = 0

    fundo_y = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    carro_velocidade = -5
                elif evento.key == pygame.K_RIGHT:
                    carro_velocidade = 5

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    carro_velocidade = 0

        tela.fill(BRANCO)




        # Movimentação do carro
        carro_x += carro_velocidade
        if carro_x < 0:
            carro_x = 0
        elif carro_x > largura - 50:
            carro_x = largura - 50

        # Movimentação do fundo
        fundo_y += 5
        if fundo_y > altura:
            fundo_y = 0

        tela.blit(fundo_imagem, (0, fundo_y - altura))
        tela.blit(fundo_imagem, (0, fundo_y))

        # Desenhar o carro
        desenhar_carro(carro_x, carro_y)

        # Desenhar os cones
        desenhar_cones(lista_cones)

        # Criar novos cones
        if lista_cones[-1][1] > 100:
            criar_cone(lista_cones)

        # Verificar colisão
        if colisao(carro_x, carro_y, lista_cones):
            mensagem("Game Over!", largura // 2, altura // 2)
            pygame.display.update()
            pygame.time.wait(2000)
            break

        # Mostrar pontos
        mensagem("Pontuação: " + str(pontos), 70, 50)

        pygame.display.update()
        pygame.time.Clock().tick(60)

# Função para mostrar mensagens na tela
def mensagem(texto, x, y):
    fonte = pygame.font.SysFont(None, 50)
    mensagem = fonte.render(texto, True, PRETO)
    tela.blit(mensagem, (x - mensagem.get_width() // 2, y - mensagem.get_height() // 2))

if __name__ == "__main__":
    jogo()
