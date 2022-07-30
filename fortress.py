import random 
from etc import Tank, windy, shoot_angle

# 쏘는 파워 함수
def shoot_power(pow):
    bomb_range = (player_angle * pow) + (wind * 10)
    return bomb_range

# 탱크 고르기
# start = input(f'탱크를 고르세요! duke or cannon : ')

# if start == 'duke':
#     pass

# 탱크 위치 세팅
tank_location = random.randrange(1, 30)
comp_location = random.randrange(150, 198)

# 게임화면 세팅 (맵, 탱크, 바람) 
map = '='*200
wind = random.randrange(-7, 7)
map_list = list(map)
map_list[tank_location], map_list[tank_location+1], map_list[tank_location+2] = '[o]', '[o]', '^'
map_list[comp_location], map_list[comp_location+1], map_list[comp_location+2] = '*', '[x]', '[x]'
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
player_bomb = shoot_power(pow)


print(player_bomb)

