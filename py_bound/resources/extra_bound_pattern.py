
def bound_stage_1(bound_pattern, bound_2, bound_3, bound_4, bound_list, screen, character_rect, bound_rects):

    check_list = []
    if bound_pattern % 26 == 1:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[6])
    if bound_pattern % 26 == 2:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
    if bound_pattern % 26 == 3:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
    if bound_pattern % 26 == 4:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))

    if bound_pattern % 26 == 14:
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[3])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[7])

    if bound_pattern % 26 == 15:
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 26 == 16:
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 26 == 17:
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
    if bound_pattern % 72 == 1:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[6])
    if bound_pattern % 72 == 2:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
    if bound_pattern % 72 == 3:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
    if bound_pattern % 72 == 4:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))

    if bound_pattern % 72 == 13:
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[3])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[7])

    if bound_pattern % 72 == 14:
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 72 == 15:
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 72 == 16:
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 72 == 23:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[6])
    if bound_pattern % 72 == 24:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
    if bound_pattern % 72 == 25:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
    if bound_pattern % 72 == 26:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))

    if bound_pattern % 72 == 34:
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[3])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[7])

    if bound_pattern % 72 == 35:
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 72 == 36:
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 72 == 37:
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 72 == 46:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[3])

    if bound_pattern % 72 == 47:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
    if bound_pattern % 72 == 48:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
    if bound_pattern % 72 == 49:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))

    if bound_pattern % 72 == 59:
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[6])
        check_list.append(bound_rects[7])

    if bound_pattern % 72 == 60:
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 72 == 61:
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 72 == 62:
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
    if bound_pattern % 128 == 1:
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[7])

    if bound_pattern % 128 == 2:
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 128 == 3:
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 128 == 4:
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 128 == 8:
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        check_list.append(bound_rects[6])

    if bound_pattern % 128 == 9:
        screen.blit(bound_2, (bound_list[6][1], 50))
    if bound_pattern % 128 == 10:
        screen.blit(bound_3, (bound_list[6][1], 50))
    if bound_pattern % 128 == 11:
        screen.blit(bound_4, (bound_list[6][1], 50))

    if bound_pattern % 128 == 15:
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        check_list.append(bound_rects[5])
    if bound_pattern % 128 == 16:
        screen.blit(bound_2, (bound_list[5][1], 50))
    if bound_pattern % 128 == 17:
        screen.blit(bound_3, (bound_list[5][1], 50))
    if bound_pattern % 128 == 18:
        screen.blit(bound_4, (bound_list[5][1], 50))

    if bound_pattern % 128 == 22:
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        check_list.append(bound_rects[4])
    if bound_pattern % 128 == 23:
        screen.blit(bound_2, (bound_list[4][1], 50))
    if bound_pattern % 128 == 24:
        screen.blit(bound_3, (bound_list[4][1], 50))
    if bound_pattern % 128 == 25:
        screen.blit(bound_4, (bound_list[4][1], 50))

    if bound_pattern % 128 == 29:
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        check_list.append(bound_rects[3])
    if bound_pattern % 128 == 30:
        screen.blit(bound_2, (bound_list[3][1], 50))
    if bound_pattern % 128 == 31:
        screen.blit(bound_3, (bound_list[3][1], 50))
    if bound_pattern % 128 == 32:
        screen.blit(bound_4, (bound_list[3][1], 50))

    if bound_pattern % 128 == 36:
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        check_list.append(bound_rects[2])
    if bound_pattern % 128 == 37:
        screen.blit(bound_2, (bound_list[2][1], 50))
    if bound_pattern % 128 == 38:
        screen.blit(bound_3, (bound_list[2][1], 50))
    if bound_pattern % 128 == 39:
        screen.blit(bound_4, (bound_list[2][1], 50))

    if bound_pattern % 128 == 43:
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        check_list.append(bound_rects[1])
    if bound_pattern % 128 == 44:
        screen.blit(bound_2, (bound_list[1][1], 50))
    if bound_pattern % 128 == 45:
        screen.blit(bound_3, (bound_list[1][1], 50))
    if bound_pattern % 128 == 46:
        screen.blit(bound_4, (bound_list[1][1], 50))

    if bound_pattern % 128 == 50:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        check_list.append(bound_rects[0])
    if bound_pattern % 128 == 51:
        screen.blit(bound_2, (bound_list[0][1], 50))
    if bound_pattern % 128 == 52:
        screen.blit(bound_3, (bound_list[0][1], 50))
    if bound_pattern % 128 == 53:
        screen.blit(bound_4, (bound_list[0][1], 50))

    if bound_pattern % 128 == 57:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[3])

    if bound_pattern % 128 == 58:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
    if bound_pattern % 128 == 59:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
    if bound_pattern % 128 == 60:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))

    if bound_pattern % 128 == 66:
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[6])
        check_list.append(bound_rects[7])
    if bound_pattern % 128 == 67:
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 128 == 68:
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 128 == 69:
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 128 == 75:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[3])
    if bound_pattern % 128 == 76:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
    if bound_pattern % 128 == 77:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
    if bound_pattern % 128 == 78:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))

    if bound_pattern % 128 == 84:
        screen.blit(bound_list[4][0], (bound_list[4][1], bound_list[4][2]))
        screen.blit(bound_list[5][0], (bound_list[5][1], bound_list[5][2]))
        screen.blit(bound_list[6][0], (bound_list[6][1], bound_list[6][2]))
        screen.blit(bound_list[7][0], (bound_list[7][1], bound_list[7][2]))
        check_list.append(bound_rects[4])
        check_list.append(bound_rects[5])
        check_list.append(bound_rects[6])
        check_list.append(bound_rects[7])
    if bound_pattern % 128 == 85:
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 128 == 86:
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 128 == 87:
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 128 == 93:
        screen.blit(bound_list[0][0], (bound_list[0][1], bound_list[0][2]))
        screen.blit(bound_list[1][0], (bound_list[1][1], bound_list[1][2]))
        screen.blit(bound_list[2][0], (bound_list[2][1], bound_list[2][2]))
        screen.blit(bound_list[3][0], (bound_list[3][1], bound_list[3][2]))
        check_list.append(bound_rects[0])
        check_list.append(bound_rects[1])
        check_list.append(bound_rects[2])
        check_list.append(bound_rects[3])
    if bound_pattern % 128 == 94:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
    if bound_pattern % 128 == 95:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
    if bound_pattern % 128 == 96:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[3][1], 50))

    if bound_pattern % 128 == 102:
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
    if bound_pattern % 128 == 103:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[2][1], 50))
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 128 == 104:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[2][1], 50))
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 128 == 105:
        screen.blit(bound_4, (bound_list[0][1], 50))
        screen.blit(bound_4, (bound_list[1][1], 50))
        screen.blit(bound_4, (bound_list[2][1], 50))
        screen.blit(bound_4, (bound_list[4][1], 50))
        screen.blit(bound_4, (bound_list[5][1], 50))
        screen.blit(bound_4, (bound_list[6][1], 50))
        screen.blit(bound_4, (bound_list[7][1], 50))

    if bound_pattern % 128 == 115:
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
    if bound_pattern % 128 == 116:
        screen.blit(bound_2, (bound_list[0][1], 50))
        screen.blit(bound_2, (bound_list[1][1], 50))
        screen.blit(bound_2, (bound_list[3][1], 50))
        screen.blit(bound_2, (bound_list[4][1], 50))
        screen.blit(bound_2, (bound_list[5][1], 50))
        screen.blit(bound_2, (bound_list[6][1], 50))
        screen.blit(bound_2, (bound_list[7][1], 50))
    if bound_pattern % 128 == 117:
        screen.blit(bound_3, (bound_list[0][1], 50))
        screen.blit(bound_3, (bound_list[1][1], 50))
        screen.blit(bound_3, (bound_list[3][1], 50))
        screen.blit(bound_3, (bound_list[4][1], 50))
        screen.blit(bound_3, (bound_list[5][1], 50))
        screen.blit(bound_3, (bound_list[6][1], 50))
        screen.blit(bound_3, (bound_list[7][1], 50))
    if bound_pattern % 128 == 118:
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