
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
stage_height = stage_size[1]  # 1인덱스가 높이다 0인덱스가 너비고 
                              # 스테이지 높이 위에 캐릭터를 두기 위해 사용, 공도 팅겨야함

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "poong.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height # 스테이지위에 놓이게


# 이벤트 루프
switch = True # 게임이 진행중인가?
while switch:
    dt = clock.tick(30) # 게임화면의 초당 프레임수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():    # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   # 오른쪽위에 창을 끄는  이벤트가 발생하였으면?
            switch = False              # 게임이 진행중이 아님

    # 3. 게임 캐릭터 위치 정의


    # 4. 충돌 처리


    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))


    pygame.display.update() # 게임화면을 다시 그리기! (while 동안 계쏙 돌면서 화면을 다시 그림 필수임!)


# pygame 종료
pygame.quit()
