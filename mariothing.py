import pygame
import time
import random
import threading
pygame.init()

#Declaring Colors
white = (255, 255, 255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 155, 0)
light_blue = (66, 182, 244)

#Displaying the main window
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

#Setting the title
pygame.display.set_caption('Marathoner!!!!!')

#Importing the images
img_big = pygame.image.load('charrun.png')
img = pygame.transform.scale(img_big, [100, 100])

cloud = pygame.image.load('cloud.png')


clock = pygame.time.Clock()
FPS = 1

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

#Allowing messages to be printed to the screen
def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width /2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)

#Importing fonts
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#Pausing
def pause():

    paused = True
    message_to_screen("Paused", black, -100, size="large")
    message_to_screen("Press C to continue or Q to quit.", black, 25)
    pygame.display.update()
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit
                    quit()
        
        clock.tick(5)

def game_intro():
    
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                    print("Hellow")
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        gameDisplay.fill(white)
        message_to_screen("Welcome to Mario thing",
                          green,
                          -100,
                          size="medium")
        message_to_screen("The objective of the game is stay alive for as long as possible",
                          black,
                          -30)
        
        message_to_screen("Dodge the obstacles",
                          black,
                          10)

        message_to_screen("And try your best",
                          black,
                          50)

        message_to_screen("Press C to play, P to pause or Q to quit",
                          black,
                          180)
        
        pygame.display.update()
        clock.tick(5)


class Clouds(threading.Thread):
    def run(self):
        cloudx = [0, 0, 0, 0, 0]
        cloudy = [0, 0, 0, 0, 0]
        for i in range(5):
            cloudx[i] = random.randint(0, 700)
            cloudy[i] = random.randint(0, 150)
            gameDisplay.blit(cloud, [cloudx[i], cloudy[i]])
            
            pygame.display.update()            
            pygame.draw.rect(gameDisplay, light_blue, [0, 0, 800, 300])
            pygame.display.update()


            

            for j in range(50):        
                for p in range(5):
                    cloudx[p] -= 25
                    gameDisplay.blit(cloud, [cloudx[p], cloudy[p]])
                    
                pygame.display.update()
                pygame.draw.rect(gameDisplay, light_blue, [0, 0, 800, 300])
                pygame.display.update()

def Jump():
    global y_value_char
    y_value_char = 400
    print("Jump")
    gameDisplay.blit(img, [100, y_value_char])
    pygame.display.update()
    time.sleep(0.25)

    pygame.draw.rect(gameDisplay, light_blue, [100, y_value_char, 100, 100])
    pygame.display.update()
    time.sleep(0.25)

    y_value_char = 200
    
    gameDisplay.blit(img, [100, y_value_char])
    pygame.display.update()
    time.sleep(0.25)

    pygame.draw.rect(gameDisplay, light_blue, [100, y_value_char, 100, 100])
    pygame.display.update()
    time.sleep(0.25)

    y_value_char = 400
    
    gameDisplay.blit(img, [100, y_value_char])
    pygame.display.update()
    time.sleep(0.25)

class ButtonPress(threading.Thread):
    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Jump()


def gameLoop():
    global gameOver
    gameOver = False
    
    print("game loop")
    global y_value_char
    global x_value

                            
    gameDisplay.fill(light_blue)
    
    
    gameDisplay.blit(img, [100, 400])
    pygame.draw.rect(gameDisplay, black, [0, 500, 800, 100])




    while gameOver == False:
        
        
            
        clouds = Clouds()
        #key_check = ButtonPress()

        clouds.start()
        #key_check.start()

        
        
        x_value = 730

        for i in range(30):
            x_value -= 30
            if x_value < 100:
                #gameOver = True
                pass
    
            pygame.draw.rect(gameDisplay, red, [x_value, 450, 50, 50])
            pygame.display.update()
            time.sleep(0.025)
            pygame.draw.rect(gameDisplay, light_blue, [x_value, 450, 50, 50])
            pygame.display.update()
            #time.sleep(0.025)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Jump()

    gameDisplay.fill(white)
    print("Game Over")
    message_to_screen("Game Over",
                        green,
                        -100,
                        size="medium")

        
        
         
        
    

    

    
        

        
        

        
 
    

    pygame.display.update()
                        
        


    
    
    clock.tick(FPS)
game_intro()
gameLoop()
