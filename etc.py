import random 

# 탱크들 세팅

class Tank:
    def __init__(self, name, dmg, hp):
        self.name = name
        self.dmg = dmg
        self.hp = hp

    def shoot(self):
        return '발사!'


duke_t = Tank('duke', 450, 2500)
cannon_t = Tank('cannon', 800, 1700)
comp_t = Tank('comp', 700, 3000)


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
        angle_num = 1
    elif 15 < angle <= 30:
        angle_num = 2
    elif 30 < angle <= 60:
        angle_num = 3
    elif 60 < angle <= 75:
        angle_num = 2
    elif 75 < angle <= 90:
        angle_num = 1
    elif 90 < angle :
        angle_num = 1

    return angle_num

# 쏘는 파워 함수
def shoot_power(pow):
    bomb_range = (player_angle * pow) + (wind * 10)
    return bomb_range