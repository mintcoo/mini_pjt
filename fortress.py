import random 
from etc.tank import Tank
from etc.wind import windy

# 1-1 탱크 고르기
# start = input(f'탱크를 고르세요! duke or cannon : ')

# if start == 'duke':
#     pass


# 1-2 화면팅 (맵, 탱크, 바람) 세팅해보자
map = '='*200
map_list = list(map)
tank_location = random.randrange(1, 30)
comp_location = random.randrange(150, 198)
map_list[tank_location], map_list[tank_location+1], map_list[tank_location+2] = '[o]', '[o]', '^'
map_list[comp_location], map_list[comp_location+1], map_list[comp_location+2] = '*', '[x]', '[x]'
map = "".join(map_list)

print('')
print(f'                                                                             ',  windy())
print('')
print('')
print('')
print('')
print('')
print('')
print(map)


    




