import pygame
import sys
import random
from time import sleep

BLACK = (0, 0, 0)
padWidth = 480     # 게임 화면의 가로 크기
padHeight = 640    # 게임 화면의 세로 크기

def initGame():
    global gamePad, clock
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')   # 게임 이름
    clock = pygame.time.Clock()

def runGame():
    global gamepad, clock

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:     # 게임 프로그램 종료
                pygame.quit()
                sys.exit()
        
        gamePad.fill(BLACK)     # 게임 화면 (검은색)

        pygame.display.update() # 게임 화면을 다시 그림

        clock.tick(60)          # 게임 화면의 초당 프레임 수를 60으로 설정
    
    pygame.quit()  # pygame 종료

initGame()
runGame()

def drawObject(obj, x, y):
    global gamePad

# 운석을 맞춘 개수 계산
def writeScore(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('파괴한 운석 수:',str(count), True, (255,255,255))
    gamePad.blit(text, (10,0))

# 운석이 화면 아래로 통과한 개수
def writePassed(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('파괴한 운석 수:',str(count), True, (255,0,0))
    gamePad.blit(text, (350,0))

# 게임 메시지 출력
def writeMessage(text):
    global gamePad
    textfont = pygame.font.Font('NanumGothic.ttf', 80)
    text = textfont.render(text, True, (255,0,0)
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