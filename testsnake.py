import pygame,sys,time,random


pygame.init()

FPS = 30

CELLWIDTH = 10
CELLHEIGHT = 10
CELLSIZE = 80
WINDOWWIDTH = CELLWIDTH * CELLSIZE
WINDOWHEIGHT = CELLHEIGHT * CELLSIZE
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."

#             R    G    B
WHITE     = (255, 255, 255)
GREY      = (200, 200, 200)
PINK      = (198, 134, 156)
BLACK     = ( 17,  18,  13)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
ORANGE    = (255, 155, 111)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0

disf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Snake Game')

snake_block = 10
clock = pygame.time.Clock()


font_style = pygame.font.SysFont('freesansbold.ttf', 30)
score_font = pygame.font.SysFont("comicsansms", 35)

def H_Score(score):
    value = score_font.render("Your Score:"+ str(score), True, DARKGRAY)
    disf.blit(value, [0,0])

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(disf, BLACK, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    mesg = font_style.render(msg,True,color)
    disf.blit(mesg, [WINDOWWIDTH/5, WINDOWHEIGHT/3])
    
def Gloop():
    
    gameover=False
    gameclose=False
    
    x1 = WINDOWWIDTH/2
    y1 = WINDOWHEIGHT/2
 
    x1_change = 0       
    y1_change = 0
    
    snake_List = []
    Length_of_snake=1
        
    foodx=round(random.randrange(0, WINDOWWIDTH - snake_block)/ 10.0)* 10.0
    foody=round(random.randrange(0, WINDOWHEIGHT - snake_block)/ 10.0)* 10.0
        
    while not gameover:
        
        
        while gameclose==True:
            disf.fill(WHITE)
            message("you lose!Press Q to Quit or C to Play again!",RED) 
            H_Score(Length_of_snake - 1)
            pygame.display.update()
                
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameover=True
                        gameclose=False
                    if event.key == pygame.K_c:
                        Gloop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-snake_block;
                    y1_change=0;
                elif event.key==pygame.K_RIGHT:
                    x1_change=snake_block;
                    y1_change=0;
                elif event.key==pygame.K_UP:
                    x1_change=0;
                    y1_change=-snake_block;
                elif event.key==pygame.K_DOWN:
                    x1_change=0;
                    y1_change=snake_block;
        if x1 >= WINDOWWIDTH or x1 < 0 or y1 >= WINDOWHEIGHT or y1 < 0:
            gameclose = True
        
        x1+=x1_change
        y1+=y1_change
        disf.fill(WHITE)
        pygame.draw.rect(disf, RED, [foodx, foody, snake_block, snake_block])
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > Length_of_snake :
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_head:
                gameclose = True
        
        snake(snake_block, snake_List)
        H_Score(Length_of_snake - 1)
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx=round(random.randrange(0, WINDOWWIDTH - snake_block)/ 10.0)* 10.0
            foody=round(random.randrange(0, WINDOWHEIGHT - snake_block)/ 10.0)* 10.0
            Length_of_snake+=1
        clock.tick(FPS)
        
    pygame.quit()
    quit()

Gloop()
