import random
poops = []
for poop in range(1, 6):
    enemy = 10
    enemy_size = (100, 100)
    enemy_width = enemy_size[0]
    enemy_height = enemy_size[1]
    enemy_x_pos = random.randrange(0, (680 - enemy_width))
    enemy_y_pos = 0
    poops.append((enemy, enemy_x_pos, enemy_y_pos))


print(poops)