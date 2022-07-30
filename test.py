import random

angle = 45

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
        angle_num = 1

    return angle_num

print(shoot_angle(angle))


    


