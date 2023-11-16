import pygame
import random
from copy import deepcopy
import time

window = pygame.display.set_mode((900, 900))

pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

class Apple:
    def __init__(self):
        self.size = (50, 50)
        self.pos = (random.randint(0, 14), random.randint(0, 14))
        
    def draw(self):
        pygame.draw.rect(window, "red", (self.pos[0]*60, self.pos[1]*60, self.size[0], self.size[1]))

class Snake:
    def __init__(self):
        self.size = (50, 50)
        self.pos = (random.randint(0, 11), random.randint(0, 11))
        self.body = [self.pos]
        self.head = self.body[-1]
        self.length = 1
        self.dirx = 1
        self.diry = 0

    def draw(self):
        for tile in self.body:
            pygame.draw.rect(window, "green", (tile[0]*60, tile[1]*60, self.size[0], self.size[1]))
            if tile == self.head:
                pygame.draw.rect(window, "darkgreen", (tile[0]*60, tile[1]*60, self.size[0], self.size[1]))

    def update(self):
        self.pos = self.pos[0] + self.dirx, self.pos[1] + self.diry
        self.body.append(self.pos)
        self.head = self.body[-1]
        if len(self.body) > self.length:
            del(self.body[0])

    def death(self):
        time.sleep(1)
        self.pos = (random.randint(0, 11), random.randint(0, 11))
        self.body = [self.pos]
        self.head = self.body[-1]
        self.length = 1
        self.dirx = 1
        self.diry = 0
        while True:
            apple.pos = (random.randint(0, 14), random.randint(0, 14))
            if apple.pos != self.head:
                break
                   
    def collision(self):
        if self.head == apple.pos:
            self.length = self.length + 1
            while True:
                apple.pos = (random.randint(0, 14), random.randint(0, 14))
                if apple.pos not in self.body:
                    break
                                
        body = deepcopy(self.body)
        body.pop()

        if self.head in body:
            self.death()
            
        if self.head[0] == -1 or self.head[0] == 15:
            self.death()
        
        if self.head[1] == -1 or self.head[1] == 15:
            self.death()
        
def makegrid(size):
    tile = size/15
    for r in range(0,15+1):
        for c in range(0,15+1):
            pygame.draw.rect(window, "white", (tile*c, tile*r, tile, tile), 1)
            
snake = Snake()
apple = Apple()

#Mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if snake.diry != 1:
                    snake.diry = -1
                    snake.dirx = 0
                break
                
            if event.key == pygame.K_a:
                if snake.dirx != 1:
                    snake.diry = 0
                    snake.dirx = -1
                break

            if event.key == pygame.K_s:
                if snake.diry != -1:
                    snake.diry = 1
                    snake.dirx = 0
                break

            if event.key == pygame.K_d:
                if snake.dirx != -1:
                    snake.diry = 0
                    snake.dirx = 1   
                break      

    snake.update()

    snake.collision()    

    window.fill("black")

    makegrid(900)

    snake.draw()

    apple.draw()

    pygame.display.flip()

    clock.tick(6)




