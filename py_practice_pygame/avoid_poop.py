import pygame
import random

#################################################################
# 기본 초기화 (반드시 해야 하는 것들)
# 초기화 ( 그냥 반드시 필요 )
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("poop")  # 게임 이름

# FPS
clock = pygame.time.Clock()
#################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경
background = pygame.image.load("resources/bground.png")

# 폰트
test_font = pygame.font.match_font('메이플스토리') # 경로 찾아주는 함수
game_font = pygame.font.Font(test_font, 20)

# 캐릭터
character = pygame.image.load("resources/poong.png")
character_size = character.get_rect().size  # 이미지 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height -2

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.3

## 적 enemy 캐릭터
poops = []
for poop in range(12):
    enemy = pygame.image.load("resources/poop.png")
    enemy_size = enemy.get_rect().size
    enemy_width = enemy_size[0]
    enemy_height = enemy_size[1]
    enemy_x_pos = random.randrange(0, (screen_width - enemy_width))
    enemy_y_pos = 0
    poops.append([enemy, enemy_x_pos, enemy_y_pos])

# 헤이스트 아이템
item_shoes = pygame.image.load("resources/item_shoes.png")
item_shoes_size = item_shoes.get_rect().size # 이미지 크기를 구해옴
item_shoes_width = item_shoes_size[0] # 아이템의 가로 크기
item_shoes_height = item_shoes_size[1] # 아이템의 세로 크기
item_shoes_x_pos = random.randrange(0, (screen_width - item_shoes_width))
item_shoes_y_pos = 0
item_shoes_speed = random.randrange(5, 9)


# 똥 스피드 
poops_speed = []
for poop in poops:
    if poop[2] == 0:
        ran = random.randrange(3, 9)
        poops_speed.append(ran)

# 점수 카운트
count = 0

# 이벤트 루프
switch = True  # 게임이 진행중인가?
while switch:
    dt = clock.tick(60)  # 게임화면의 초당 프레임수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 오른쪽위에 창을 끄는  이벤트가 발생하였으면?
            switch = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += character_speed

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    ## 위에서 뽑은 똥리스트에서 각 높이값이 680넘으면 재생성
    
    for k, poop in enumerate(poops):
        if poop[2] > screen_height:
            #여기가 새로 생성하는곳이니까 여기서 짜야되는데 
            poop[1] = random.randrange(0, (screen_width - enemy_width))
            poop[2] = 0
            count += 1
            # 아래 enumerate를 이용하는게 핵심
            poops_speed[k] = random.randint(3, 9)

    # 아이템 새로 생성하는 곳
    if item_shoes_y_pos > screen_height: 
        item_shoes_x_pos = random.randrange(0, (screen_width - enemy_width))
        item_shoes_y_pos = 0
        # 아래 enumerate를 이용하는게 핵심
        item_shoes_speed = random.randint(5, 9)

    
            

    character_x_pos += to_x * dt
    ## 리스트 첫 시작 위치 차이..?

    #여기서 poops_speed 배열 선언하고 길이0개 값이아무것도없어서
    # if poop[2] == 0:
        
    # 각 똥들 속도 개별로 설정
    i = 0
    for poop in poops:
        poop[2] += poops_speed[i] # 이 코드가 속도 설정하는데
        i += 1 

    # 헤이스트 속도
    item_shoes_y_pos += item_shoes_speed

    # 3. 게임 캐릭터 위치 정의

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:  # ★캐릭터 크기만큼 빼줘야 끝에 그려진다!
        character_x_pos = screen_width - character_width

    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ## 적과의 충돌 포문
    enemy_rects = []
    for poop in poops:
        enemy_rect = poop[0].get_rect()
        enemy_rect.left = poop[1]
        enemy_rect.top = poop[2]
        enemy_rects.append(enemy_rect)

    # 아이템과의 충돌
    item_shoes_rect = item_shoes.get_rect()
    item_shoes_rect.left = item_shoes_x_pos
    item_shoes_rect.top = item_shoes_y_pos


    # 충돌 체크
    for rect in enemy_rects:
        if character_rect.colliderect(rect):
            print("충돌함")
            switch = False

    # 아이템 충돌 (먹음)
    if character_rect.colliderect(item_shoes_rect):
        print("속도업!!")
        item_shoes_y_pos = -8000
        character_speed = 0.5

    if item_shoes_y_pos == -2000:
        character_speed = 0.3


    # 5. 화면에 그리기
    count_draw = game_font.render(str(f'Scores : {count}'), True, (255, 255, 255 ))


    screen.blit(background, (0, 0))  # 배경 그리기 (좌표 0, 0 이 제일왼쪽위)

    screen.blit(character, (character_x_pos, character_y_pos))  # 계속 캐릭터를 그림

    screen.blit(item_shoes, (item_shoes_x_pos, item_shoes_y_pos))

    
    for poop in poops:
        screen.blit(poop[0], (poop[1], poop[2]))  # 적 그리기
    
    screen.blit(count_draw, (10, 10))

    pygame.display.update()  # 게임화면을 다시 그리기! (while 동안 계쏙 돌면서 화면을 다시 그림 필수임!)

pygame.time.delay(2000)  # 2초 정도 대기 (ms)

# pygame 종료
pygame.quit()
