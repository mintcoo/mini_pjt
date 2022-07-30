import random 

# 탱크들 세팅

class Tank:
    def __init__(self, name, dmg, hp, missile):
        self.name = name
        self.dmg = dmg
        self.hp = hp
        self.missile = missile

    def shoot_power(self, pow, player_angle, wind):
        self.bomb_range = (player_angle * pow)//2 + (wind * 10)
        return self.bomb_range



# duke_t = Tank('duke', 450, 2500, 3)
# cannon_t = Tank('cannon', 800, 1700, 1)
# com_t = Tank('comp', 700, 3000, 3)


# 바람 세팅 함수

def windy(wind):
    if wind == 0:
        return 'Damage x 2!'
    elif wind < 0:
        return '<'*(abs(wind))
    elif wind > 0:
        return '>'*(abs(wind))

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

