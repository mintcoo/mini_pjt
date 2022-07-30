import random 

# 바람 세팅 함수

def windy():
    wind = random.randrange(-7, 7)
    if wind == 0:
        return 'Damage x 2!'
    elif wind < 0:
        return '<'*(abs(wind))
    elif wind > 0:
        return '>'*(abs(wind))
