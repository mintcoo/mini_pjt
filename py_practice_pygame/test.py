import random
import pygame
# poops = []
# for poop in range(1, 6):
#     enemy = 10
#     enemy_size = (100, 100)
#     enemy_width = enemy_size[0]
#     enemy_height = enemy_size[1]
#     enemy_x_pos = random.randrange(0, (680 - enemy_width))
#     enemy_y_pos = 0
#     poops.append([enemy, enemy_x_pos, enemy_y_pos])

# print(poops)

# # print(poops)
# test = [[10, 53, 0], [10, 262, 0], [10, 511, 0], [10, 110, 0], [10, 285, 0]]
# asd = []

# for poop in test:
#     if poop[2] == 0:
#         ran = random.randrange(1, 5)
#         asd.append(ran)

# print(asd)
# i = 0
# for poop in test:
#     poop[2] += asd[i]
#     i += 1

# print(test)


# test2 = ['ab','c','df','g']

# for k, i in enumerate(test2):
#     print(k, i)

for i in pygame.font.get_fonts():
    print(i)