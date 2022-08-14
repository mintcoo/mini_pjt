import os
import pygame

#################################################################
# 기본 초기화 (반드시 해야 하는 것들)
# 초기화 ( 그냥 반드시 필요 )
pygame.init() 

# 화면 크기 설정
screen_width = 640 
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height)) 

# 화면 타이틀 설정
pygame.display.set_caption("PPPang") # 게임 이름

# FPS
clock = pygame.time.Clock()
#################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치를 반환
image_path = os.path.join(current_path, "resources", "images") # images폴더의 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기 (배경위에 스테이지가 있어서 그위에서 움직이는거)
stage = pygame.image.load(os.path.join(image_path, "brown_stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 1인덱스가 높이다 0인덱스가 너비고 
                             # 스테이지 높이 위에 캐릭터를 두기 위해 사용, 공도 팅겨야함

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "poong.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height # 스테이지위에 놓이게

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기

weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 공 만들기(4개 크기에 대해 따로 처리) 리스트로 관리
ball_images = [
    pygame.image.load(os.path.join(image_path, "ball_1.png")),
    pygame.image.load(os.path.join(image_path, "ball_2.png")),
    pygame.image.load(os.path.join(image_path, "ball_3.png")),
    pygame.image.load(os.path.join(image_path, "ball_4.png"))
]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9] # index 0, 1, 2, 3 에 해당하는 값

# 공들
balls = []

# 최초 발생하는 큰 공 추가
balls.append({
    "pos_x" : 50, # 공의 x 좌표
    "pos_y" : 50, # 공의 y 좌표
    "img_idx" : 0, # 처음 제일 큰 공은 인덱스 0 으로 시작
    "to_x" : 3, # 공의 x축 이동방향, -3 이면 왼쪽, 3이면 오른쪽
    "to_y" : -6, # y축 이동방향
    "init_spd_y" : ball_speed_y[0]}) # y 최초속도



# 이벤트 루프
switch = True # 게임이 진행중인가?
while switch:
    dt = clock.tick(30) # 게임화면의 초당 프레임수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():     # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:    # 오른쪽위에 창을 끄는  이벤트가 발생하였으면?
            switch = False               # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:        # 캐릭터를 왼쪽으로 
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:     # 캐릭터를 오른쪽으로 
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:     # 무기 발사, 무기는 캐릭터 중앙에서 나옴
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])  # 여러발 쏘기위해 리스트형태로 추가
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    # 100, 200 에서 x는 그대로 y좌표는 180, 160, 140, ... 줄어들게..
    # 무기 스피드만큼 줄어들어야한다.
    weapons = [ [w[0], (w[1] - weapon_speed) ] for w in weapons if w[1] > 0 ] # 무기 위치를 위로
    
    # 천장에 닿은 무기 없애기
    # 위에서 만든 무기중 아직 천장에 닿지 않은 거에 대해서만 
    # 리스트 만들어 다시 저장(천장에 닿으면 사라짐)
    # weapons = [ [w[0], w[1]]  for w in weapons if w[1] > 0 ]

    
    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]





    # 4. 충돌 처리


    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    # 무기 그리는 위치가 캐릭터 보다 아래서 나와야 함!
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    


    pygame.display.update() # 게임화면을 다시 그리기! (while 동안 계쏙 돌면서 화면을 다시 그림 필수임!)


# pygame 종료
pygame.quit()
