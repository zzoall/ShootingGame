import pygame
import sys
import random
from time import sleep

BLACK = (0, 0, 0)
padWidth = 480     # 게임 화면의 가로 크기
padHeight = 640    # 게임 화면의 세로 크기

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))

def initGame():
    global gamePad, clock, background
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')          # 게임 이름
    background = pygame.image.load('background.png')  # 배경 그림
    fighter = pygame.image.load('fighter.png')        # 전투기 그림
    missile = pygame.image.load('missile.png')        # 미사일 그림
    clock = pygame.time.Clock()

def runGame():
    global gamepad, clock, background, fighter, missile

    # 전투기 크기
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    # 전투기 초기 위치 (x, y)
    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0

    missileXY = []

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:     # 게임 프로그램 종료
                pygame.quit()
                sys.exit()
            
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:    # 전투기 왼쪽으로 이동
                    fighterX -= 5
                
                elif event.key == pygame.K_RIGHT: # 전투기 오른쪽으로 이동
                    fighterX += 5

                elif event.key == pygame.K_SPACE: # 미사일 발사
                    missileX = x + fighterWidth/2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])
            
            if event.type in [pygame.KEYUP]:    # 방향기를 떼면 전투기가 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0
        
        drawObject(background, 0, 0)    # 메인 화면 그리기

        # 전투기 위치 재조정
        x += fighterX
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth

        drawObject(fighter, x, y)  # 비행기를 게임 화면의 (x, y) 좌표에 그림
        
        gamePad.fill(BLACK)     # 게임 화면 (검은색)

        pygame.display.update() # 게임 화면을 다시 그림

        clock.tick(60)          # 게임 화면의 초당 프레임 수를 60으로 설정
    
    pygame.quit()  # pygame 종료

initGame()
runGame()



# 운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('파괴한 운석 수:',str(count), True, (255,255,255))
    gamePad.blit(text, (10,0))

# 운석을 놓친 개수 계산
def writePassed(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('파괴한 운석 수:',str(count), True, (255,0,0))
    gamePad.blit(text, (350,0))

# 운석이 화면 아래로 통과한 개수
def writePassed(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('놓친 운석 :' + str(count), True, (255,0,0))
    gamePad.blit(text, (360,0))

# 게임 메시지 출력
def writeMessage(text):
    global gamePad
    textfont = pygame.font('NanumGothic.ttf', 80)
    text = textfont.render(text, True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    sleep(2)
    runGame()

# 전투기가 운석과 충돌했을 때 메시지 출력
def crash():
    global gamePad
    writeMessage('전투기 파괴!')
    
# 게임 오버 메시지 보이기
def gameOver():
    global gamePad
    writeMessage('게임 오버!')