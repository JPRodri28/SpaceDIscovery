import pygame
from pygame.locals import *
from tkinter import simpledialog
import math

icon = pygame.image.load("space.png")
pygame.init()
tamanho = (1000, 563)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_icon(icon)
fundo = pygame.image.load("bg.jpg")
branco = (255, 255, 255)
fonte = pygame.font.Font(None, 20)
bolinhas = []
linhas = []
raio_bola = 5
pygame.mixer.music.load("Space_Machine_Power.mp3")
pygame.mixer.music.play(-1)
running = True
linha_ativa = False
posicao_inicial = None
posicao_final = None
arquivo_estrelas = "estrelas.txt"
def carregar_estrelas():
    bolinhas.clear()
    linhas.clear()
    with open(arquivo_estrelas, "r") as arquivo:
        for linha in arquivo:
            posicao_x, posicao_y, legenda = linha.strip().split(",")
            posicao = (int(posicao_x), int(posicao_y))
            bolinha = {
                "posicao": posicao,
                "legenda": legenda
            }
            bolinhas.append(bolinha)
            if len(bolinhas) >= 2:
                posicao_anterior = bolinhas[-2]["posicao"]
                posicao_atual = bolinha["posicao"]
                linha = (posicao_anterior, posicao_atual)
                linhas.append(linha)

def salvar_estrelas():
    with open(arquivo_estrelas, "w") as arquivo:
        for bolinha in bolinhas:
            posicao_x = str(bolinha["posicao"][0])
            posicao_y = str(bolinha["posicao"][1])
            legenda = bolinha["legenda"]
            arquivo.write(posicao_x + "," + posicao_y + "," + legenda + "\n")
def calcular_distancia(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distancia
while running:
    tela.blit(fundo, (0, 0))
    texto_salvar = fonte.render("Pressione F10 para salvar", True, branco)
    tela.blit(texto_salvar, (10, 10))
    texto_carregar = fonte.render("Pressione F11 para carregar as estrelas", True, branco)
    tela.blit(texto_carregar, (10, 30))
    texto_excluir = fonte.render("Pressione F12 para excluir", True, branco)
    tela.blit(texto_excluir, (10, 50))
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            salvar_estrelas()
            running = False
        elif evento.type == KEYDOWN and evento.key == K_ESCAPE:
            salvar_estrelas()
            running = False
        elif evento.type == KEYDOWN and evento.key == K_F10:
            salvar_estrelas()
        elif evento.type == KEYDOWN and evento.key == K_F11:
            carregar_estrelas()
        elif evento.type == MOUSEBUTTONDOWN:
            if evento.button == 1:
                posicao_bola = evento.pos
                if tela.get_rect().collidepoint(posicao_bola):
                    item = simpledialog.askstring("Space", "Nome da Estrela:")
                    if item == "":
                        item = "desconhecido " + str(posicao_bola[0]) + "," + str(posicao_bola[1])
                    bolinha = {
                        "posicao": posicao_bola,
                        "legenda": item
                    }
                    bolinhas.append(bolinha)
                    if len(bolinhas) >= 2:
                        posicao_anterior = bolinhas[-2]["posicao"]
                        posicao_atual = bolinha["posicao"]
                        linha = (posicao_anterior, posicao_atual)
                        linhas.append(linha)
                    if linha_ativa:
                        linha_ativa = False
                        posicao_inicial = None
                        posicao_final = None
                    else:
                        linha_ativa = True
                        posicao_inicial = posicao_bola
        elif evento.type == MOUSEBUTTONUP:
            if evento.button == 1:
                posicao_final = evento.pos
        elif evento.type == KEYDOWN and evento.key == K_F12: 
            resposta = simpledialog.askstring("Space", "Tem certeza que deseja excluir tudo? (S/N):")
            if resposta and resposta.lower() == "s":
                bolinhas.clear()
                linhas.clear()
                with open(arquivo_estrelas, "w") as arquivo:
                    arquivo.write("")
    for bolinha in bolinhas:
        posicao_bola = bolinha["posicao"]
        legenda = bolinha["legenda"]
        pygame.draw.circle(tela, branco, posicao_bola, raio_bola)
        posicao_legenda = (posicao_bola[0] + raio_bola + 5, posicao_bola[1] - raio_bola)
        texto_legenda = fonte.render(legenda, True, branco)
        tela.blit(texto_legenda, posicao_legenda)
    
    for linha in linhas:
        posicao_inicial, posicao_final = linha
        distancia_x = abs(posicao_final[0] - posicao_inicial[0])
        distancia_y = abs(posicao_final[1] - posicao_inicial[1])
        distancia_total = distancia_x + distancia_y
        pygame.draw.line(tela, branco, posicao_inicial, posicao_final, 1)
        texto_distancia = fonte.render(str(distancia_total), True, branco)
        posicao_texto = ((posicao_inicial[0] + posicao_final[0]) // 2, (posicao_inicial[1] + posicao_final[1]) // 2)
        tela.blit(texto_distancia, posicao_texto)
    
    if linha_ativa and posicao_inicial and posicao_final:
        pygame.draw.line(tela, branco, posicao_inicial, posicao_final, 1)
    
    pygame.display.flip()

pygame.quit()
