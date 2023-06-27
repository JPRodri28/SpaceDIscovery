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
