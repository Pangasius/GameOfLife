import numpy as np
import pygame
import time
import random

#make a board
square = 100

board = np.zeros((square, square, 2))

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
    # load and set the logo
    logo = pygame.image.load("logo32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("A Game")
     
    # create a surface on screen that has the size of the board
    screen = pygame.display.set_mode((square*10,square*10))
     

    #image for animation
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

    resets()

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

def resets() :
    #clears the number of alive blocks
    for i in range(square) :
        for j in range(square) :
            board[i,j,1] = 0

def randomize() :
    global screen
    global imageone
    #creates a random board
    for i in range(square) :
        for j in range(square) :
            if random.randint(0,1) * random.randint(0,1) * random.randint(0,1) == 1 :
                screen.blit(imageone, (i*10,j*10))
                board[i,j,0] = 1
            else :
                board[i,j,0] = 0
            
def check() :
    #analyse surroundings and count alive blocks
    for i in range(square-2) :
        for j in range(square-2) :
            if j < square :
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
    while running :

        #trying to fixed frames
        t = time.process_time()

        #checks for a key
        keypressed = pygame.key.get_pressed()

        #for the mouse
        done = False

        #animation
        pygame.event.pump()
        
        #create a pattern
        if keypressed[pygame.K_a] :
            #get the mouse position to alternate beetween two states
            mouseposX = pygame.mouse.get_pos()[0]  // 10
            mouseposY = pygame.mouse.get_pos()[1]  // 10
            if (mouseposX >= 0 and mouseposX <= square and mouseposY >= 0 and mouseposY <= square) :
                print(mouseposX, "  " ,mouseposY)
                if  (board[mouseposX,mouseposY,0] == 0 and done == False) :
                    board[mouseposX,mouseposY,0] = 1
                    done = True
                if  (board[mouseposX,mouseposY,0] == 1 and done == False) :
                    board[mouseposX,mouseposY,0] = 0
                    done = True

                #get it to be seen
                for i in range(square) :
                    for j in range (square) :
                        if board[i,j,0] == 1 :
                            screen.blit(imageone, (i*10,j*10))
                        else :
                            screen.blit(imagetwo, (i*10,j*10))
                    
        if keypressed[pygame.K_q] :
            print("a")
            activate()
        if keypressed[pygame.K_t] :
            print("randomizing ...")
            randomize()
            activate()
            time.sleep(0.5)
        #refresh
        pygame.display.flip()
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        #time follow up
        dt = time.process_time()
        delay = dt - t
        if delay > 1/20 :
            print(delay)
        if delay < 4/10 :
            time.sleep(0.5 - delay)
        

#execution

main()
visual()
