import pygame as pg
import random

imgItem = pg.image.load("rocket.png")
imgItem2 = pg.image.load("star.png")
imgItem3 = pg.image.load("tartaruga.png")


class Item:
    def __init__(self, win, x, y, largura, altura, vel, cor):
        self.win = win
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.vel = vel
        self.cor = cor

    def draw(self):
        self.win.blit(imgItem, (self.x, self.y))

    def move(self):
        self.y += self.vel
        if self.y > 600:
            self.x = random.randint(0, 800)
            self.y = -self.altura

class Item2:
    def __init__(self, win, x, y, largura, altura, vel, cor):
        self.win = win
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.vel = vel
        self.cor = cor

    def draw(self):
        self.win.blit(imgItem2, (self.x, self.y))

    def move(self):
        self.y += self.vel
        if self.y > 600:
            self.x = random.randint(0, 800)
            self.y = -self.altura

class Item3:
    def __init__(self, win, x, y, largura, altura, vel, cor):
        self.win = win
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.vel = vel
        self.cor = cor

    def draw(self):
        self.win.blit(imgItem3, (self.x, self.y))

    def move(self):
        self.y += self.vel
        if self.y > 600:
            self.x = random.randint(0, 800)
            self.y = -self.altura
