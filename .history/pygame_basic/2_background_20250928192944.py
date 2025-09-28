
import pygame

pygame.init() #초기화 (반드시 필요)

screen_width = 480 #가로크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 배경 이미지 불러오기
background = pygame.image.load("./pygame_basic/background.png")

clock = pygame.time.Clock()
#event loop
running = True #게임이 진행중인가?

while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수를 설정
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님
        else : 
            pygame.display.update()
    
    # screen.fill((0,0,255)); #색상으로 채우기
    screen.blit(background,(0,0)) #배경 그리기
    pygame.display.update() # 화면을 매프레임 업데이트
    


# pygame 종료
pygame.quit()

