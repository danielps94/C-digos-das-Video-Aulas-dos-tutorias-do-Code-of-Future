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
pygame.display.set_caption("Esquiva de Obstáculos")

# Carregamento de imagens
nave_imagem = pygame.image.load('nave.png')
nave_imagem = pygame.transform.scale(nave_imagem, (50, 50))

obstaculo_imagem = pygame.image.load('obstaculo.png')
obstaculo_imagem = pygame.transform.scale(obstaculo_imagem, (50, 50))

# Função para desenhar a nave
def desenhar_nave(x, y):
    tela.blit(nave_imagem, (x, y))

# Função para desenhar os obstáculos
def desenhar_obstaculos(lista_obstaculos):
    for obstaculo in lista_obstaculos:
        tela.blit(obstaculo_imagem, (obstaculo[0], obstaculo[1]))

# Função para criar novos obstáculos
def criar_obstaculo(lista_obstaculos):
    x = random.randrange(0, largura - 50)
    y = -50
    lista_obstaculos.append([x, y])

# Função para verificar colisão
def colisao(nave_x, nave_y, lista_obstaculos):
    for obstaculo in lista_obstaculos:
        if nave_x + 50 > obstaculo[0] and nave_x < obstaculo[0] + 50:
            if nave_y < obstaculo[1] + 50 and nave_y + 50 > obstaculo[1]:
                return True
    return False

# Loop principal do jogo
def jogo():
    nave_x = largura // 2 - 25
    nave_y = altura - 100
    nave_velocidade = 0

    lista_obstaculos = []

    pontos = 0

    clock = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    nave_velocidade = -5
                elif evento.key == pygame.K_RIGHT:
                    nave_velocidade = 5

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    nave_velocidade = 0

        tela.fill(BRANCO)

        # Movimentação da nave
        nave_x += nave_velocidade
        if nave_x < 0:
            nave_x = 0
        elif nave_x > largura - 50:
            nave_x = largura - 50

        # Desenhar a nave
        desenhar_nave(nave_x, nave_y)

        # Desenhar os obstáculos
        desenhar_obstaculos(lista_obstaculos)

        # Criar novos obstáculos
        if random.randrange(0, 100) < 3:
            criar_obstaculo(lista_obstaculos)

        # Verificar colisão
        if colisao(nave_x, nave_y, lista_obstaculos):
            mensagem("Game Over!", largura // 2, altura // 2)
            pygame.display.update()
            pygame.time.wait(2000)
            return

        # Atualizar pontos
        pontos += 1

        # Mostrar pontos
        mensagem("Pontuação: " + str(pontos), 70, 50)

        pygame.display.update()
        clock.tick(60)

# Função para mostrar mensagens na tela
def mensagem(texto, x, y):
    fonte = pygame.font.SysFont(None, 50)
    mensagem = fonte.render(texto, True, PRETO)
    tela.blit(mensagem, (x - mensagem.get_width() // 2, y - mensagem.get_height() // 2))

if __name__ == "__main__":
    jogo()
