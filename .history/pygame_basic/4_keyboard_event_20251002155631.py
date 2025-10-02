
import pygame

pygame.init() #초기화 (반드시 필요)

screen_width = 480 #가로크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 배경 이미지 불러오기
background = pygame.image.load("./pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("./pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width * 0.5) - (character_width * 0.5) #화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0


# FPS
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

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                # character_x_pos -= 5
                to_x -= 5
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                # character_x_pos += 5
                to_x += 5
            elif event.key == pygame.K_UP: #캐릭터를 위로
                # character_y_pos -= 5
                to_y -= 5
            elif event.key == pygame.K_DOWN: #캐릭터를 아래로
                # character_y_pos += 5
                to_y += 5
    
    screen.blit(background,(0,0)) #배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터 그리기

    pygame.display.update() # 화면을 매프레임 업데이트
    


# pygame 종료
pygame.quit()

