import random
import re

def parse(dice_str) -> (int, int):
    match = re.match(r'^(\d+)d(\d+)$', dice_str)
    if match:
        a = int(match.group(1))
        b = int(match.group(2))
        return a, b
    else:
        return None


def roll(number, sides):
    """

    :param number: 投掷次数
    :param sides: 面数
    :return:
    """
    score = 0
    for i in range(number):
        score += random.randint(1, sides)
    return score

def d20(advantage=0):
    """

    1 优势
    2 劣势
    :param advantage: 是否有优势
    :return:
    """
    point = roll(1, 20)
    if advantage == 0:
        return point
    elif advantage == 1:
        new_point = roll(1, 20)
        if new_point > point:
            return new_point
        else:
            return point
    elif advantage == 2:
        new_point = roll(1, 20)
        if new_point > point:
            return point
        else:
            return new_point
