import random


i = 0
for i in range(3):
    wind = random.randrange(-7, 7)
    i += 1
    print(wind)
    if wind == 0:
        print('◎')
    elif wind < 0:
        print ('<'*(abs(wind)))
    elif wind > 0:
        print ('>'*(abs(wind)))

    


