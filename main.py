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
