import random 
from etc import Tank, windy, shoot_angle

# 쏘는 파워 함수
# def shoot_power(pow):
#     bomb_range = (player_angle * pow) + (wind * 10)
#     return bomb_range

# 탱크 고르기
while True:
    print('')
    print('duke :【 DMG : 450 】【 missile : 3발 】【 hp : 2500 】')
    print('cannon :【 DMG : 800 】【 missile : 1발 】【 hp : 1700 】')
    print('')
    start = input(f'탱크를 고르세요! :  ')

    if start == 'duke':
        duke_t = Tank('duke', 450, 2500, 3)
        com_t = Tank('comp', 700, 3000, 3)
        break

    elif start == 'cannon':
        cannon_t = Tank('cannon', 800, 1700, 1)
        com_t = Tank('comp', 700, 3000, 3)
        break
    else:
        print('*'*47)
        print('*'*8, '  제대로 탱크를 입력바람!!!  ', '*'*8)
        print('*'*47)
        continue
    

# 탱크 위치 및 바람 세팅

tank_location = random.randrange(1, 30)
com_location = random.randrange(150, 198)

round = 1
switch = True
# 게임화면 세팅 (맵, 탱크, 바람) 
while switch == True:
    wind = random.randrange(-7, 7)
    map = '='*200
    map_list = list(map)
    map_list[tank_location], map_list[tank_location+1], map_list[tank_location+2] = '[o]', '[o]', '^'
    map_list[com_location], map_list[com_location+1], map_list[com_location+2] = '*', '[x]', '[x]'
    map = "".join(map_list)

    print('')
    print(' '*90,  windy(wind))
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print(map)

# 플레이어 턴
    ang = int(input(f'당신 차례입니다. 각도를 입력해주세요 (0 ~ 90): '))
    pow = int(input(f'당신 차례입니다. 파워를 입력해주세요 (max : 100): '))

    player_angle = shoot_angle(ang)
    player_bomb = duke_t.shoot_power(pow, player_angle, wind) + (tank_location+2)
    print(player_bomb)

    if 0 <= player_bomb <= 198 :
        map = '='*200
        map_list = list(map)
        map_list[tank_location], map_list[tank_location+1], map_list[tank_location+2] = '[o]', '[o]', '^'
        map_list[com_location], map_list[com_location+1], map_list[com_location+2] = '*', '[x]', '[x]'
        map_list[player_bomb], map_list[player_bomb+1], map_list[player_bomb+2] = 'W' 'W' 'W'
        map = "".join(map_list)

        print('')
        print(' '*90,  windy(wind))
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print(map)
        switch = False

     
    elif player_bomb >= 198 :
        print('홈런입미다 개못쏨 ㅋㅋ')
        print('')
        switch = False

        
    elif player_bomb < 0:
        print('뒤로 날아감 ㅋㅋ 레전드ㅋㅋ')
        print('')
        switch = False

    

# 컴퓨터 턴
    input(f'컴퓨터 차례입니다. enter를 입력해주세요: ')
    com_pow = random.randrange(0, tank_location+50-round)

    map = '='*200
    map_list = list(map)
    map_list[tank_location], map_list[tank_location+1], map_list[tank_location+2] = '[o]', '[o]', '^'
    map_list[com_location], map_list[com_location+1], map_list[com_location+2] = '*', '[x]', '[x]'
    map_list[com_pow], map_list[com_pow+1], map_list[com_pow+2] = 'W' 'W' 'W'
    map = "".join(map_list)

    print('')
    print(' '*90,  windy(wind))
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print(map)
    print('')
    print(f'『 {round}라운드 결과 』')
    print(f'Player HP : {duke_t.hp} ')
    print(f'Computer HP : {com_t.hp} ')
    print('')
    input(f'다음 라운드를 시작하려면. enter를 입력해주세요: ')
    round += 1
    switch = True

# 이제 데미지 깎이는거 해야함!
