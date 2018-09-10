import numpy as np
import pygame
import time
import random

#change here the time beetween cycles !!! if the time is longer or shorter, it will be difficult to switch the state of cells
fixedframes = 0.4 #in sec (the invert gives you the frames/sec)

#make a square board of the following dimensions
square = 75
board = np.zeros((square, square, 2))

#read the number of iteration
iteration = 0

#all states are set to 0 to begin with
for i in range(square) :
    for j in range (square) :
        board[i,j,0] = 0

# define a variable to control the main loop
running = True

# define a main function
def main() :
    global screen
    global imagetwo
    global imageone

    # initialize the pygame module
    pygame.init()
    # load and set the logo (32x32) 
    logo = pygame.image.load("logo32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Life and Death") #anything you want
     
    # create a surface on screen that has the size of the board
    screen = pygame.display.set_mode((square*10,square*10))
     

    #image for animation MUST BE 10x10 pixels or change all the 10 by the other dimension
    imageone = pygame.image.load("Alive.png")
    imagetwo = pygame.image.load("Dead.png")

    #first step
    for i in range(square) :
        for j in range (square) :
            if board[i,j,0] == 1 :
                screen.blit(imageone, (i*10,j*10))
            else :
                screen.blit(imagetwo, (i*10,j*10))



def activate() :
    global screen
    global imagetwo
    global imageone

    check()
    
    for i in range(square) :
        for j in range (square) :
            #change of color
            if board[i,j,1] > 3 or board[i,j,1] < 2 :
                board[i,j,0] = 0
            if board[i,j,1] == 3 :
                board[i,j,0] = 1
            if board[i,j,0] == 1 :
                screen.blit(imageone, (i*10,j*10))
            else :
                screen.blit(imagetwo, (i*10,j*10))

def check() :
    #analyse surroundings and count alive blocks
    for i in range(square-2) :
        for j in range(square-2) :
            if j < square :
                board[i,j,1] = 0
                if board[i-1,j-1,0] == 1 :
                    board[i,j,1] = board[i,j,1] + 1
                if board[i-1,j,0] == 1 :
                    board[i,j,1] = board[i,j,1] + 1
                if board[i-1,j+1,0] == 1 :
                    board[i,j,1] = board[i,j,1] + 1
                if board[i,j-1,0] == 1 :
                    board[i,j,1] = board[i,j,1] + 1
                if board[i,j+1,0] == 1 :
                    board[i,j,1] = board[i,j,1] + 1
                if board[i+1,j-1,0] == 1 :
                    board[i,j,1] = board[i,j,1] + 1
                if board[i+1,j,0] == 1 :
                    board[i,j,1] = board[i,j,1] + 1
                if board[i+1,j+1,0] == 1 :
                    board[i,j,1] = board[i,j,1] + 1

def visual() :
    global running
    global iteration
    global fixedframes
    while running :

        #trying to fixed frames
        t = time.process_time()

        #checks for a key
        keypressed = pygame.key.get_pressed()

        #animation
        pygame.event.pump()
        
        #create a pattern
        if keypressed[pygame.K_a] :
            #get the mouse position to alternate beetween two states
            mouseposX = pygame.mouse.get_pos()[0]  // 10
            mouseposY = pygame.mouse.get_pos()[1]  // 10
            if (mouseposX >= 0 and mouseposX <= square and mouseposY >= 0 and mouseposY <= square) :
                casestate = board[mouseposX,mouseposY,0]
                if  casestate == 1 :
                    board[mouseposX,mouseposY,0] = 0
                if  casestate == 0 :
                    board[mouseposX,mouseposY,0] = 1

                #get it to be seen
                for i in range(square) :
                    for j in range (square) :
                        if board[i,j,0] == 1 :
                            screen.blit(imageone, (i*10,j*10))
                        else :
                            screen.blit(imagetwo, (i*10,j*10))
                    
        if keypressed[pygame.K_q] :
            iteration = iteration + 1
            print(iteration)
            activate()
        #refresh
        pygame.display.flip()
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        #fixed frames follow up
        dt = time.process_time()
        delay = dt - t
        if delay > 1/20 :
            print(delay)
        if delay <= fixedframes :
            time.sleep(fixedframes - delay)
        

#execution
main()
visual()
