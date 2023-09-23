
#game name: click the square
#date 9/23/2023
#creator: tony kim



import pygame
import sys
import random

import time


pygame.init()

screen_width = 1000 #screen building
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("AimLab")

white = (255, 255, 255)  #color making
red = (255, 0, 0)
black = (0, 0, 0)
score = 0

square_width = 50 #making of square
square_height = 50
square_x = (screen_width - square_width) //2
square_y = (screen_height - square_height) //2

running = True
start_time = time.time() #starting time of the game

while running:
    elapsed_time = time.time()-start_time 
    for event in pygame.event.get(): 
        if score >= 10:
            print("Your final score is", elapsed_time) #final score
            running = False
        if event.type == pygame.QUIT: #if you quit the game the game stops running
            running = False  
        if event.type == pygame.MOUSEBUTTONDOWN : #if you click on teh square you get one more point
            x, y = event.pos 
            if (x>=square_x and x<square_x+square_width) and (y>= square_y and y<square_y+square_height):
                square_x = random.randint(0, screen_width)
                square_y = random.randint(0, screen_height)
                score = score + 1 #score adds up
                
            else:
                print("You lost") #you lost
                running = False
    screen.fill(black)
    font1 = pygame.font.SysFont(None,30) 
    img1 = font1.render(str(score), True, white) #text of score
    img2 = font1.render(str(round(elapsed_time, 1)), True, white) #text of time
    screen.blit(img1, (50,50)) 
    screen.blit(img2, (50, 100) )
    pygame.draw.rect(screen, red, [square_x, square_y, square_width, square_height]) #color of square
    pygame.display.update()


    
pygame.quit() #exit
sys.exit()

    
