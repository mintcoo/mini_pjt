
def bound_stage_1(bound_pattern, bound_2, bound_3, bound_4, bound_list, screen, character_rect, bound_rects):

    check_list = []
    if bound_pattern % 13 == 1:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[6])
    if bound_pattern % 13 == 2:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
    if bound_pattern % 13 == 3:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
    if bound_pattern % 13 == 4:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))

    if bound_pattern % 13 == 7:
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[3])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[7])

    if bound_pattern % 13 == 8:
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 13 == 9:
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 13 == 10:
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    for rect in check_list:
        rect_result = character_rect.colliderect(rect)
        if rect_result:
            return rect_result


def bound_stage_2(bound_pattern, bound_2, bound_3, bound_4, bound_list, screen, character_rect, bound_rects):

    check_list = []
    if bound_pattern % 36 == 1:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[6])
    if bound_pattern % 36 == 2:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
    if bound_pattern % 36 == 3:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
    if bound_pattern % 36 == 4:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))

    if bound_pattern % 36 == 7:
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[3])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[7])

    if bound_pattern % 36 == 8:
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 36 == 9:
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 36 == 10:
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 36 == 13:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[6])
    if bound_pattern % 36 == 14:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
    if bound_pattern % 36 == 15:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
    if bound_pattern % 36 == 16:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))

    if bound_pattern % 36 == 19:
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[3])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[7])

    if bound_pattern % 36 == 20:
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 36 == 21:
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 36 == 22:
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 36 == 24:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[3])

    if bound_pattern % 36 == 25:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
    if bound_pattern % 36 == 26:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
    if bound_pattern % 36 == 27:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))

    if bound_pattern % 36 == 33:
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[6])
        check_list.append(bound_rects[7])

    if bound_pattern % 36 == 34:
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 36 == 35:
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 36 == 36:
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    for rect in check_list:
        rect_result = character_rect.colliderect(rect)
        if rect_result:
            return rect_result


def bound_stage_3(bound_pattern, bound_2, bound_3, bound_4, bound_list, screen, character_rect, bound_rects):

    check_list = []
    if bound_pattern % 80 == 1:
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[7])

    if bound_pattern % 80 == 2:
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 80 == 3:
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 80 == 4:
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 80 == 5:
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        check_list.append(bound_rects[6])

    if bound_pattern % 80 == 6:
        screen.blit(bound_2, (bound_list[6][1], 50))
    if bound_pattern % 80 == 7:
        screen.blit(bound_3, (bound_list[6][1], 50))
    if bound_pattern % 80 == 8:
        screen.blit(bound_4, (bound_list[6][1], 50))

    if bound_pattern % 80 == 9:
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        check_list.append(bound_rects[5])
    if bound_pattern % 80 == 10:
        screen.blit(bound_2, (bound_list[5][1], 50))
    if bound_pattern % 80 == 11:
        screen.blit(bound_3, (bound_list[5][1], 50))
    if bound_pattern % 80 == 12:
        screen.blit(bound_4, (bound_list[5][1], 50))

    if bound_pattern % 80 == 13:
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        check_list.append(bound_rects[4])
    if bound_pattern % 80 == 14:
        screen.blit(bound_2, (bound_list[4][1], 50))
    if bound_pattern % 80 == 15:
        screen.blit(bound_3, (bound_list[4][1], 50))
    if bound_pattern % 80 == 16:
        screen.blit(bound_4, (bound_list[4][1], 50))

    if bound_pattern % 80 == 17:
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        check_list.append(bound_rects[3])
    if bound_pattern % 80 == 18:
        screen.blit(bound_2, (bound_list[3][1], 50))
    if bound_pattern % 80 == 19:
        screen.blit(bound_3, (bound_list[3][1], 50))
    if bound_pattern % 80 == 20:
        screen.blit(bound_4, (bound_list[3][1], 50))

    if bound_pattern % 80 == 21:
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        check_list.append(bound_rects[2])
    if bound_pattern % 80 == 22:
        screen.blit(bound_2, (bound_list[2][1], 50))
    if bound_pattern % 80 == 23:
        screen.blit(bound_3, (bound_list[2][1], 50))
    if bound_pattern % 80 == 24:
        screen.blit(bound_4, (bound_list[2][1], 50))

    if bound_pattern % 80 == 25:
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        check_list.append(bound_rects[1])
    if bound_pattern % 80 == 26:
        screen.blit(bound_2, (bound_list[1][1], 50))
    if bound_pattern % 80 == 27:
        screen.blit(bound_3, (bound_list[1][1], 50))
    if bound_pattern % 80 == 28:
        screen.blit(bound_4, (bound_list[1][1], 50))

    if bound_pattern % 80 == 29:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        check_list.append(bound_rects[0])
    if bound_pattern % 80 == 30:
        screen.blit(bound_2, (bound_list[0][1], 50))
    if bound_pattern % 80 == 31:
        screen.blit(bound_3, (bound_list[0][1], 50))
    if bound_pattern % 80 == 31:
        screen.blit(bound_4, (bound_list[0][1], 50))



    if bound_pattern % 80 == 32:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[3])

    if bound_pattern % 80 == 33:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
    if bound_pattern % 80 == 34:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
    if bound_pattern % 80 == 35:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))
    if bound_pattern % 80 == 38:
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[6])
        check_list.append(bound_rects[7])

    if bound_pattern % 80 == 39:
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 80 == 40:
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 80 == 41:
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 80 == 44:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[3])
    if bound_pattern % 80 == 45:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
    if bound_pattern % 80 == 46:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
    if bound_pattern % 80 == 47:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))
    if bound_pattern % 80 == 50:
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[6])
        check_list.append(bound_rects[7])

    if bound_pattern % 80 == 51:
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 80 == 52:
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 80 == 53:
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 80 == 56:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[3])
    if bound_pattern % 80 == 57:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
    if bound_pattern % 80 == 58:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
    if bound_pattern % 80 == 59:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))

    if bound_pattern % 80 == 63:
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
    if bound_pattern % 80 == 64:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 80 == 65:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 80 == 66:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 80 == 70:
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
    if bound_pattern % 80 == 71:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 80 == 72:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 80 == 73:
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