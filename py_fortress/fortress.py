import random 
from etc import Tank, windy, shoot_angle, tank_dmg

# 탱크 고르기
while True:
    print('')
    print('duke :【 DMG : 450 】【 missile : 3발 】【 hp : 2500 】')
    print('cannon :【 DMG : 800 】【 missile : 1발 】【 hp : 1700 】')
    print('')
    start = input(f'탱크를 고르세요! :  ')
    print('')
    if start == 'duke':
        player_t = Tank('duke', 550, 2500, 3)    

    elif start == 'cannon':
        player_t = Tank('cannon', 1100, 1700, 1)

    else:
        print('*'*47)
        print('*'*8, '  제대로 탱크를 입력바람!!!  ', '*'*8)
        print('*'*47)
        continue
    level = input('난이도를 고르셈 normal / hard : ')
    if level == 'normal':
        com_t = Tank('baby', 600, 3000, 3)
        break

    elif level == 'hard':
        com_t = Tank('boss', 800, 4500, 3)
        break
    else:
        print('*'*47)
        print('*'*8, '  제대로 난이도 입력바람!!!  ', '*'*8)
        print('*'*47)
        continue    

# 탱크 위치 및 바람 세팅

tank_location = random.randrange(1, 20)
com_location = random.randrange(90, 102)

round = 1
switch = True
# 게임화면 세팅 (맵, 탱크, 바람) 
while switch == True:
    wind = random.randrange(-7, 7)
    map = '〓'*110
    map_hp = '〓'*105
    map_list = list(map)
    map_hp_list = list(map_hp)
    map_list[tank_location], map_list[tank_location+1], map_list[tank_location+2] = '[o]', '[o]', '//'
    map_list[com_location], map_list[com_location+1], map_list[com_location+2] = '\\\\', '[x]', '[x]'
    map_hp_list[tank_location] = f' Hp:{player_t.hp} '
    map_hp_list[com_location-2] = f' Hp:{com_t.hp} '
    map = "".join(map_list)
    map_hp = "".join(map_hp_list)
    print('')
    print('')
    print(' '*10, '☆',' '*120, '★')
    print(' '*30, '*',' '*167, '*', ' '*7, )
    print(' '*50, '＊', ' '*104,'☽',' '*49 )
    print(' '*95, '§ ', windy(wind),' §' )
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print(map)
    print(map_hp)

# 플레이어 턴
    print('')
    ang = int(input(f'당신 차례입니다. 각도를 입력해주세요 (0 ~ 90): '))
    pow = int(input(f'당신 차례입니다. 파워를 입력해주세요 (max : 100): '))
    if pow > 100:
        pow = 100
    elif pow < 0:
        pow = 0

    player_angle = shoot_angle(ang)
    player_bomb = player_t.shoot_power(pow, player_angle, wind) + (tank_location+2)

    if 0 <= player_bomb <= 102 :
        map = '〓'*110
        map_hp = '〓'*105
        map_list = list(map)
        map_hp_list = list(map_hp)
        map_list[tank_location], map_list[tank_location+1], map_list[tank_location+2] = '[o]', '[o]', '//'
        map_list[com_location], map_list[com_location+1], map_list[com_location+2] = '\\\\', '[x]', '[x]'
        if start == 'duke':
            map_list[player_bomb], map_list[player_bomb+1], map_list[player_bomb+2] = '▽' '▽' '▽'
        elif start == 'cannon':
            map_list[player_bomb] = '★'
        map_hp_list[tank_location] = f' Hp:{player_t.hp} '
        map_hp_list[com_location-2] = f' Hp:{com_t.hp} '
        map = "".join(map_list)
        map_hp = "".join(map_hp_list)
        print('')
        print('')
        print(' '*10, '☆',' '*120, '★')
        print(' '*30, '*',' '*167, '*', ' '*7, )
        print(' '*50, '＊', ' '*104,'☽',' '*49 )
        print(' '*95, '§ ', windy(wind),' §' )
        print('')
        print('')
        print('')
        print('')
        print('')
        print('')
        print(map)
        print(map_hp)
        com_t.hp = tank_dmg(player_bomb, com_location, player_t.dmg, com_t.hp, player_t.missile)
        if com_t.hp < 0 :
            com_t.hp = 0
            print(f'『 {round}라운드 결과 』')
            print(f'Player HP : {player_t.hp} ')
            print(f'Computer HP : {com_t.hp} ')
            print('')
            print('@@ 겨우 승리하였습니다!! @@')
            break
        switch = False

     
    elif player_bomb >= 103 :
        print('홈런입미다 개못쏨 ㅋㅋ')
        print('')
        switch = False

        
    elif player_bomb < 0:
        print('뒤로 날아감 ㅋㅋ 레전드ㅋㅋ')
        print('')
        switch = False

    

# 컴퓨터 턴
    print('')
    input(f'컴퓨터 차례입니다. 아무키나 입력해주세요: ')
    com_pow = random.randrange(0, tank_location+30-round)

    map = '〓'*110
    map_hp = '〓'*105
    map_list = list(map)
    map_hp_list = list(map_hp)
    map_list[tank_location], map_list[tank_location+1], map_list[tank_location+2] = '[o]', '[o]', '//'
    map_list[com_location], map_list[com_location+1], map_list[com_location+2] = '\\\\', '[x]', '[x]'
    map_list[com_pow], map_list[com_pow+1], map_list[com_pow+2] = '♨' '♨' '♨'
    map_hp_list[tank_location] = f' Hp:{player_t.hp} '
    map_hp_list[com_location-2] = f' Hp:{com_t.hp} '
    map = "".join(map_list)
    map_hp = "".join(map_hp_list)

    print('')
    print('')
    print(' '*10, '☆',' '*120, '★')
    print(' '*30, '*',' '*167, '*', ' '*7, )
    print(' '*50, '＊', ' '*104,'☽',' '*49 )
    print(' '*95, '§ ', windy(wind),' §' )
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print(map)
    print(map_hp)    
    print('')
    player_t.hp = tank_dmg(com_pow, tank_location, com_t.dmg, player_t.hp, com_t.missile)
    if player_t.hp < 0 :
        player_t.hp = 0
        print(f'『 {round}라운드 결과 』')
        print(f'Player HP : {player_t.hp} ')
        print(f'Computer HP : {com_t.hp} ')
        print('')
        print('ㅋㅋ GG! 쳐발리셨습니다!! ㅋㅋ')
        break
    
    print(f'『 {round}라운드 결과 』')
    print(f'Player HP : {player_t.hp} ')
    print(f'Computer HP : {com_t.hp} ')
    print('')
    input(f'다음 라운드를 시작하려면. 아무키나 입력해주세요: ')
    round += 1
    switch = True

    # 맵상에 hp표시, 아이템?