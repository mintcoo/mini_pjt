

def bound_1(bound_pattern, bound_2, bound_3, bound_4, bound_list, screen, character_rect, bound_rects):

    check_list = []
    if bound_pattern % 64 == 1:
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[7])

    if bound_pattern % 64 == 2:
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 64 == 3:
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 64 == 4:
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 64 == 5:
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        check_list.append(bound_rects[6])

    if bound_pattern % 64 == 6:
        screen.blit(bound_2, (bound_list[6][1], 50))
    if bound_pattern % 64 == 7:
        screen.blit(bound_3, (bound_list[6][1], 50))
    if bound_pattern % 64 == 8:
        screen.blit(bound_4, (bound_list[6][1], 50))

    if bound_pattern % 64 == 9:
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        check_list.append(bound_rects[5])
    if bound_pattern % 64 == 10:
        screen.blit(bound_2, (bound_list[5][1], 50))
    if bound_pattern % 64 == 11:
        screen.blit(bound_3, (bound_list[5][1], 50))
    if bound_pattern % 64 == 12:
        screen.blit(bound_4, (bound_list[5][1], 50))

    if bound_pattern % 64 == 13:
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        check_list.append(bound_rects[4])
    if bound_pattern % 64 == 14:
        screen.blit(bound_2, (bound_list[4][1], 50))
    if bound_pattern % 64 == 15:
        screen.blit(bound_3, (bound_list[4][1], 50))
    if bound_pattern % 64 == 16:
        screen.blit(bound_4, (bound_list[4][1], 50))

    if bound_pattern % 64 == 17:
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        check_list.append(bound_rects[3])
    if bound_pattern % 64 == 18:
        screen.blit(bound_2, (bound_list[3][1], 50))
    if bound_pattern % 64 == 19:
        screen.blit(bound_3, (bound_list[3][1], 50))
    if bound_pattern % 64 == 20:
        screen.blit(bound_4, (bound_list[3][1], 50))

    if bound_pattern % 64 == 21:
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        check_list.append(bound_rects[2])
    if bound_pattern % 64 == 22:
        screen.blit(bound_2, (bound_list[2][1], 50))
    if bound_pattern % 64 == 23:
        screen.blit(bound_3, (bound_list[2][1], 50))
    if bound_pattern % 64 == 24:
        screen.blit(bound_4, (bound_list[2][1], 50))

    if bound_pattern % 64 == 25:
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        check_list.append(bound_rects[1])
    if bound_pattern % 64 == 26:
        screen.blit(bound_2, (bound_list[1][1], 50))
    if bound_pattern % 64 == 27:
        screen.blit(bound_3, (bound_list[1][1], 50))
    if bound_pattern % 64 == 28:
        screen.blit(bound_4, (bound_list[1][1], 50))

    if bound_pattern % 64 == 29:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        check_list.append(bound_rects[0])
    if bound_pattern % 64 == 30:
        screen.blit(bound_2, (bound_list[0][1], 50))
    if bound_pattern % 64 == 31:
        screen.blit(bound_3, (bound_list[0][1], 50))
    if bound_pattern % 64 == 31:
        screen.blit(bound_4, (bound_list[0][1], 50))



    if bound_pattern % 64 == 32:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[3])

    if bound_pattern % 64 == 33:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
    if bound_pattern % 64 == 34:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
    if bound_pattern % 64 == 35:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))
    if bound_pattern % 64 == 36:
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[6])
        check_list.append(bound_rects[7])

    if bound_pattern % 64 == 37:
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 64 == 38:
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 64 == 39:
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 64 == 40:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[3])
    if bound_pattern % 64 == 41:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
    if bound_pattern % 64 == 42:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
    if bound_pattern % 64 == 43:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))
    if bound_pattern % 64 == 44:
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[6])
        check_list.append(bound_rects[7])

    if bound_pattern % 64 == 45:
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 64 == 46:
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 64 == 47:
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 64 == 48:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[3])
    if bound_pattern % 64 == 49:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
    if bound_pattern % 64 == 50:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
    if bound_pattern % 64 == 51:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))

    if bound_pattern % 64 == 52:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[6])
        check_list.append(bound_rects[7])
    if bound_pattern % 64 == 53:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 64 == 54:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 64 == 55:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 64 == 58:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[3])
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[6])
        check_list.append(bound_rects[7])
    if bound_pattern % 64 == 59:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 64 == 60:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 64 == 61:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))


    for rect in check_list:
        rect_result = character_rect.colliderect(rect)
        if rect_result:
            return rect_result

