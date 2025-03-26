import dice
import core

_crit = 2


def attak(modifier, ac, advantage=0) -> int:
    """
    攻击检定\n
    0 = 失败 1 = 成功 2 = 重击
    :param advantage: 优势
    :param modifier: 关键属性调整值
    :param ac: 护甲等级
    :return:
    """
    # d20
    base_point = dice.d20(advantage)
    if base_point == 20:
        return _crit
    elif base_point == 1:
        return 0
    # 调整值
    point = base_point + modifier
    # AC对比
    if point >= ac:
        return 1
    else:
        return 0


def damage(number, sides, modifier, critical: int) -> int:
    """
    伤害骰

    :param number:
    :param sides:
    :param modifier:
    :param critical: 是否重击
    :return:
    """
    if critical == _crit:
        point = dice.roll(number*2, sides)
    elif critical == 0:
        point = 0
    else:
        point = dice.roll(number, sides)
    return point + modifier


def saving(dc, modifier, advantage=0) -> int:
    """
    豁免检定

    0 = 失败 1 = 成功
    :param advantage: 1 优势 2 劣势
    :param dc: 难度等级
    :param modifier: 豁免属性调整值
    :return:
    """
    base_point = dice.d20(advantage)
    if base_point + modifier >= dc:
        return 1
    else:
        return 0


def spell_attack(number, sides, saving_flag=0) -> int:
    base_damage = dice.roll(number, sides)
    point = 0
    if saving_flag == 1:
        point = base_damage // 2
    elif saving_flag == 0:
        point = base_damage
    return point


if __name__ == '__main__':
    # 火球术
    ability_modifier = 0  # 关键施法属性调整值
    proficiency = 2  # 熟练项加值
    spell_dc = 8 + ability_modifier + proficiency
    modi = 0
    sav = saving(spell_dc, modi)
    print(spell_attack(8, 6, sav))