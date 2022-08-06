import random 

# 탱크들 세팅

class Tank:
    def __init__(self, name, dmg, hp, missile):
        self.name = name
        self.dmg = dmg
        self.hp = hp
        self.missile = missile

    def shoot_power(self, pow, player_angle, wind):
        self.bomb_range = (player_angle * pow)//4 + (wind)
        return self.bomb_range



# duke_t = Tank('duke', 450, 2500, 3)
# cannon_t = Tank('cannon', 800, 1700, 1)
# com_t = Tank('comp', 700, 3000, 3)


# 바람 세팅 함수

def windy(wind):
    if wind == 0:
        return '☀'
    elif wind < 0:
        return '◀ '*(abs(wind))
    elif wind > 0:
        return '▶ '*(abs(wind))

# 각도 세팅 가중치 함수
def shoot_angle(angle):
    if angle <= 0:
        angle_num = 1
    elif 0 < angle <= 15:
        angle_num = 2
    elif 15 < angle <= 30:
        angle_num = 3
    elif 30 < angle <= 60:
        angle_num = 4
    elif 60 < angle <= 75:
        angle_num = 3
    elif 75 < angle <= 90:
        angle_num = 2
    elif 90 < angle :
        angle_num = -1

    return angle_num


# 탱크 데미지에 따른 hp 계산함수
def tank_dmg(hit_point, location, dmg, hp, missile):
    if hit_point == location:
        print(f'『 적중! {dmg * missile} 데미지!! 』')  # 1발짜리는 데미지 1번 3발짜리는 데미지 3번
        print( '')
        hp -= dmg * missile
          
    elif hit_point == location+1  and missile == 1:    # 1발짜리일때 컴퓨터위치 +1 자리 맞으면 데미지
        print(f'『 적중! {dmg * missile} 데미지!! 』')
        print( '')
        hp -= dmg * missile

    elif hit_point == location+2  and missile == 1:    # 1발짜리일때 컴퓨터위치 +2 자리 맞으면 데미지
        print(f'『 적중! {dmg * missile} 데미지!! 』')
        print( '')
        hp -= dmg * missile
        
    elif hit_point == location+1  or hit_point == location-1 and missile == 3:  #  3발짜리일때 컴퓨터 위치 +1 이나 -1 맞추면 2발히트!
        print(f'『 적중! {dmg * (missile-1)} 데미지!! 』')
        print( '')
        hp -= dmg * (missile -1)
        
    elif hit_point == location+2 or hit_point == location-2 and missile == 3: #  3발짜리일때 컴퓨터 위치 +2 이나 -2 맞추면 1발히트!
        print(f'『 적중! {dmg } 데미지!! 』')
        print( '')
        hp -= dmg
    return hp