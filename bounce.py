#Bounce
import pygame #game library for python
import random #for random positioning of objects

#initiate pygame
pygame.init() 

#screen ratio
screen_width = 1040
screen_height = 680

#create screen
screen = pygame.display.set_mode((screen_width,screen_height)) 

#create objects for game
player = pygame.image.load("player.jpg")
prize = pygame.image.load("prize.jpg")
enemy1 = pygame.image.load("monster.jpg")
enemy2 = pygame.image.load("monster.jpg")
enemy3 = pygame.image.load("monster.jpg")


#Get width and height of objects
player_h = player.get_height()
player_w = player.get_width()

prize_h = prize.get_height()
prize_w = prize.get_width()

enemy1_h = enemy1.get_height()
enemy1_w = enemy1.get_width()

enemy2_h = enemy2.get_height()
enemy2_w = enemy2.get_width()

enemy3_h = enemy3.get_height()
enemy3_w = enemy3.get_width()


#scale the objects down to half their size
player = pygame.transform.scale(player, (int(player_w/2), int(player_h/2)))
prize = pygame.transform.scale(prize, (int(prize_w/2), int(prize_h/2)))
enemy1 = pygame.transform.scale(enemy1, (int(enemy1_w/2), int(enemy1_h/2)))
enemy2 = pygame.transform.scale(enemy2, (int(enemy2_w/2), int(enemy2_h/2)))
enemy3 = pygame.transform.scale(enemy3, (int(enemy3_w/2), int(enemy3_h/2)))


#set start positions (to random points)
player_y = random.randint(0, screen_height-player_h)
player_x = random.randint(0, screen_width-player_w-700) #some variables manipulated to prevent collisions before the game even starts

prize_y = random.randint(0, screen_height-prize_h)
prize_x = random.randint(520, screen_width-prize_w)

enemy1_y = random.randint(0, screen_height-enemy1_h)
enemy1_x = random.randint(400, screen_width-enemy1_w)

enemy2_y = random.randint(0, screen_height-enemy2_h)
enemy2_x = random.randint(400, screen_width-enemy2_w)

enemy3_y = random.randint(0, screen_height-enemy3_h)
enemy3_x = random.randint(400, screen_width-enemy3_w)


#initial choice of -1 or 1 for directional movement of enemy objects
movement = [-1,1]
dir_enemy1_y = random.choice(movement)
dir_enemy1_x = random.choice(movement)
dir_enemy2_y = random.choice(movement)
dir_enemy2_x = random.choice(movement)
dir_enemy3_y = random.choice(movement)
dir_enemy3_x = random.choice(movement)


#declare booleans for keys and set them initially to false
up_key = False
down_key = False
left_key = False
right_key = False


#speed of enemy objects
enemy1_speed = 0.35
enemy2_speed = 0.35
enemy3_speed = 0.35


#Beginning of game loop
while 1:

    #clear screen
    screen.fill(0) 
    
    #draw the objects and position them at the specificied co-ordinates
    screen.blit(player, (player_x, player_y))
    screen.blit(prize, (prize_x, prize_y))
    screen.blit(enemy1, (enemy1_x, enemy1_y))
    screen.blit(enemy2, (enemy2_x, enemy2_y))
    screen.blit(enemy3, (enemy3_x, enemy3_y))
    
    #update the screen
    pygame.display.flip()
    
    #sequence to determine if an input is being given
    for event in pygame.event.get():
        
        #close the screen if the user is trying to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        #check if user is pressing down a key
        if event.type == pygame.KEYDOWN:
            #assign press down value as true if necessary
            if event.key == pygame.K_UP:
                up_key = True
            if event.key == pygame.K_DOWN:
                down_key = True
            if event.key == pygame.K_LEFT:
                left_key = True
            if event.key == pygame.K_RIGHT:
                right_key = True
        
        #check if user has released the key
        if event.type == pygame.KEYUP:
            #assign press down value as false if necessary
            if event.key == pygame.K_UP:
                up_key = False
            if event.key == pygame.K_DOWN:
                down_key = False
            if event.key == pygame.K_LEFT:
                left_key = False
            if event.key == pygame.K_RIGHT:
                right_key = False
    
    #move in direction of key(s) pressed
    if up_key == True:
        if player_y > 0:
            player_y -= 1
    if down_key == True:
        if player_y < screen_height - (player_h/2): #divided by 2 because of scale
            player_y += 1
    if left_key == True:
        if player_x > 0:
            player_x -= 1
    if right_key == True:
        if player_x < screen_width - (player_w/2):
            player_x += 1
            
    #create bounding box for objects
    player_box = pygame.Rect(player.get_rect())
    player_box.top = player_y
    player_box.left = player_x
    
    prize_box = pygame.Rect(prize.get_rect())
    prize_box.top = prize_y
    prize_box.left = prize_x
    
    enemy1_box = pygame.Rect(enemy1.get_rect())
    enemy1_box.top = enemy1_y
    enemy1_box.left = enemy1_x
    
    enemy2_box = pygame.Rect(enemy2.get_rect())
    enemy2_box.top = enemy2_y
    enemy2_box.left = enemy2_x
    
    enemy3_box = pygame.Rect(enemy3.get_rect())
    enemy3_box.top = enemy3_y
    enemy3_box.left = enemy3_x
   
    #use bounding box to check for collisions
    if player_box.colliderect(prize_box):
        print("You Win!")
        # Quite game and exit window: 
        pygame.quit()
        exit(0)
    
    if player_box.colliderect(enemy1_box) or player_box.colliderect(enemy2_box) or player_box.colliderect(enemy3_box):
        print("You lose!")
        # Quite game and exit window: 
        pygame.quit()
        exit(0)
    
    #change the direction and increase the speed if an enemy object touches a screen boundary
    
    #x boundaries
    if enemy1_x <= 0 or enemy1_x>=screen_width-(enemy1_w/2): #divided by 2 because the images are half their original size
        dir_enemy1_x=dir_enemy1_x*-1
        enemy1_speed+=0.15
    if enemy2_x <= 0 or enemy2_x>=screen_width-(enemy2_w/2):
        dir_enemy2_x=dir_enemy2_x*-1
        enemy2_speed+=0.15
    if enemy3_x <= 0 or enemy3_x>=screen_width-(enemy3_w/2):
        dir_enemy3_x=dir_enemy3_x*-1
        enemy3_speed+=0.15
    
    #y boundaries    
    if enemy1_y <= 0 or enemy1_y>=screen_height-(enemy1_h/2):
        dir_enemy1_y=dir_enemy1_y*-1
    if enemy2_y <= 0 or enemy2_y>=screen_height-(enemy2_h/2):
        dir_enemy2_y=dir_enemy2_y*-1
    if enemy3_y <= 0 or enemy3_y>=screen_height-(enemy3_h/2):
        dir_enemy3_y=dir_enemy3_y*-1
    
    #change the object's position and velocity
    enemy1_y +=dir_enemy1_y*enemy1_speed
    enemy1_x +=dir_enemy1_x*enemy1_speed
    enemy2_y +=dir_enemy2_y*enemy2_speed
    enemy2_x +=dir_enemy2_x*enemy2_speed
    enemy3_y +=dir_enemy3_y*enemy3_speed
    enemy3_x +=dir_enemy3_x*enemy3_speed


#References:

#Information that helped with understanding random.randint:
#https://pynative.com/python-random-randrange/

#Information that assisted to figure out how to scale an object's size
#pygame.org/docs/ref/transform.html#pygame.transform.scale2x

#Page that assisted with understanding lists and the random.choice method:
#https://stackoverflow.com/questions/306400/how-can-i-randomly-select-an-item-from-a-list