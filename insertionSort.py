from random import randint
import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 400
setCount = 500
t = WIDTH/setCount

clock = pygame.time.Clock()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("INSERTION SORT")
font = pygame.font.SysFont("comicsans", 24)

def draw(mat, index, marker1, marker2, swapColor):
    for i in range(index):
        #pygame.draw.circle(win, (255,255,255), ((t*i), mat[i]), (t/2))
        #pygame.draw.circle(win, swapColor, ((t*marker), mat[marker]), (t/2))
        #pygame.draw.circle(win, swapColor, ((t*(marker+1)), mat[marker+1]), (t/2))

        pygame.draw.rect(win, (255,255,255), ((t*i),0,t,mat[i]))
        pygame.draw.rect(win, swapColor, ((t*marker1),0,t,mat[marker1]))
        pygame.draw.rect(win, swapColor, ((t*marker2),0,t,mat[marker2]))

def play(mat, index, run):

    iterations = 0
    inserts = 0
    FPS = 60
    pause = False

    while run:

        for i in range(1, index):
            percent = ((i+1)/index)*100
            text1 = font.render("ITERATIONS: "+str(iterations), True, (255,255,255))
            text2 = font.render("INSERTS: "+str(inserts), True, (255,255,255))
            text3 = font.render("LEFT: reduces F.P.S.  |   RIGHT: increases F.P.S.   |   DOWN: pauses   |   UP: unpauses", True, (255,255,255))
            text4 = font.render(str(round(percent, 1)), True, (255,255,255))
            text5 = font.render("% sorted", True, (255,255,255))
            swapColor = (0, 255, 0)
            key = mat[i]
            j = i-1
            while j >= 0 and key < mat[j]:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                speedInp = pygame.key.get_pressed()
                if speedInp[pygame.K_LEFT]:
                    FPS -= 2
                elif speedInp[pygame.K_RIGHT]:
                    FPS += 2
                elif speedInp[pygame.K_DOWN]:
                    pause = True

                while pause:

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()

                    unpause = pygame.key.get_pressed()
                    if unpause[pygame.K_UP]:
                        pause = False

                iterations += 1
                clock.tick(FPS)

                mat[j+1] = mat[j]
                j -= 1

                win.fill((0,0,0))
                draw(mat, index, j, i, swapColor)
                win.blit(text1,(100, 350))
                win.blit(text2,(400, 350))
                win.blit(text3,(100, 370))
                win.blit(text4,(700, 350))
                win.blit(text5,(745, 350))
                pygame.display.update()

            if mat[j+1] != key:
                swapColor = (255, 0, 0)
                inserts += 1
                swapsound = pygame.mixer.Sound('sounds/swap.wav')
                pygame.mixer.Sound.play(swapsound)
                pygame.mixer.music.stop()
            mat[j+1] = key
            win.fill((0,0,0))
            draw(mat, index, j, i, swapColor)    
            win.blit(text1,(100, 350))
            win.blit(text2,(400, 350))
            win.blit(text3,(100, 370))
            win.blit(text4,(700, 350))
            win.blit(text5,(745, 350))
            pygame.display.update()
            
        win.fill((0,0,0))
        draw(mat, index, -2, -2, (0, 255, 0))
        win.blit(text1,(100, 350))
        win.blit(text2,(300, 350))
        win.blit(text4,(700, 350))
        win.blit(text5,(745, 350))
        endtext = font.render("PRESS 'SPACE' TO RESTART", True, (255,255,255))
        win.blit(endtext, (100, 370))
        pygame.display.update()
        run = False

def main():

    N = setCount
    a = []
    for i in range(N):
        num = randint(5, 300)
        a.append(num)
    run = False
    start = True
    
    while start:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            run = True
            start = False
        else:
            draw(a, N, -2, -2, (0, 255, 0))
            starttext = font.render("PRESS 'SPACE' TO START", True, (255,255,255))
            win.blit(starttext, (100, 350))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

        pygame.display.update()

    play(a, N, run)

    end = True
    while end:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            a = []
            for i in range(N):
                num = randint(5, 300)
                a.append(num)
            run = True
            play(a, N, run)
        else:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

    clock.tick(30)
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
main()
