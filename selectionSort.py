from random import randint
import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 400
setCount = 500
t = WIDTH/setCount

clock = pygame.time.Clock()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SELECTION SORT")
font = pygame.font.SysFont("comicsans", 24)

def draw(mat, index, marker, lowest, swapColor, rep, line):
    for i in range(index):
        if rep == 0:
            pygame.draw.circle(win, (255,255,255), ((t*i), mat[i]), (t/2))
        elif rep == 1:
            pygame.draw.rect(win, (255,255,255), ((t*i),0,t,mat[i]))

        if line == 0:
            pygame.draw.circle(win, swapColor, ((t*marker), mat[marker]), (t/2))
            pygame.draw.circle(win, swapColor, ((t*lowest), mat[lowest]), (t/2))
        elif line == 1:
            pygame.draw.rect(win, swapColor, ((t*marker),0,t,mat[marker]))
            pygame.draw.rect(win, swapColor, ((t*lowest),0,t,mat[lowest]))

def play(mat, index, run):

    iterations = 0
    swaps = 0
    FPS = 60
    pause = False
    rep = 1
    signM = -1
    line = 1
    signL = -1

    while run:

        for i in range(index-1):
            swapColor = (0, 255, 0)
            minIndex = i
            for j in range(i+1, index):
                if mat[minIndex] > mat[j]:
                    minIndex = j
            percent = (i/(index-2))*100
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
            elif speedInp[pygame.K_s]:
                rep = rep + (signM)
                signM = -signM
            elif speedInp[pygame.K_m]:
                line = line + (signL)
                signL = -signL

            while pause:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                unpause = pygame.key.get_pressed()
                if unpause[pygame.K_UP]:
                    pause = False

            iterations += 1
            clock.tick(FPS)

            swapColor = (255, 0, 0)    
            swaps += 1
            swapsound = pygame.mixer.Sound('sounds/swap.wav')
            pygame.mixer.Sound.play(swapsound)
            pygame.mixer.music.stop()
            temp = mat[minIndex]
            mat[minIndex] = mat[i]
            mat[i] = temp

            win.fill((0,0,0))
            draw(mat, index, i, minIndex, swapColor, rep, line)
            text1 = font.render("ITERATIONS: "+str(iterations), True, (255,255,255))
            text2 = font.render("SWAPS: "+str(swaps), True, (255,255,255))
            text3 = font.render("LEFT: reduces F.P.S.  |   RIGHT: increases F.P.S.   |   DOWN: pauses   |   UP: unpauses", True, (255,255,255))
            text4 = font.render("s: Swaps between line and circle representation  |   m: Shows and removes marker line    ", True, (255,255,255))
            text5 = font.render(str(round(percent, 1)), True, (255,255,255))
            text6 = font.render("% sorted", True, (255,255,255))
                
            win.blit(text1,(100, 330))
            win.blit(text2,(400, 330))
            win.blit(text3,(100, 350))
            win.blit(text4,(100, 370))
            win.blit(text5,(700, 330))
            win.blit(text6,(745, 330))
            pygame.display.update()
            
        win.fill((0,0,0))
        draw(mat, index, -2, -2, (0, 255, 0), rep, line)
        win.blit(text1,(100, 350))
        win.blit(text2,(300, 350))
        win.blit(text5,(700, 350))
        win.blit(text6,(745, 350))
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
            draw(a, N, -2, -2, (0, 255, 0), 1, 1)
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
