def dice_roll(dice_num, dice_face):
    result = []
    int(dice_num)
    int(dice_face)
    for _ in range(0, dice_num):
        result.append(random.randint(1, dice_face))
    return result