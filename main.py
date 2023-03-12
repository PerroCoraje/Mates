import pygame
import asyncio
import colider
import pygbag, asyncio

pygame.init()

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
screen=pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
map_imagen=pygame.image.load("images/mapa.jpg").convert()
boatb_imagen=pygame.image.load("images/boat_b.png").convert_alpha()
boatg_imagen=pygame.image.load("images/boat_g.png").convert_alpha()


boatg_x = 180 
boatg_y = 100
al1 = 50
anch1 = 50

boatb_x = 550
boatb_y = 580
al2 = 50
anch2 = 50   



async def simulación():
    global boatg_y, boatb_x, boatb_y, boatg_x,al1,al2,anch1,anch2
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  
                 running=False
    
        if colider.colider(boatg_x, boatg_y, al1, al2, anch1, anch2, boatb_x, boatb_y):
                pygame.time.delay(7000)
                break

        boatg_y += 1
        boatb_x -= 1.5
        boatb_y -= 1

        screen.blit(map_imagen,(0,0))
        screen.blit(boatb_imagen,(boatb_x,boatb_y))
        screen.blit(boatg_imagen,(boatg_x,boatg_y))    

        pygame.display.update()
        pygame.time.delay(10)
        await asyncio.sleep(0)

simulación()

asyncio.run(simulación())


