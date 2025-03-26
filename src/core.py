import random
import json
import os


advantage = 1
disadvantage = 2


def st(filename, attr, value):
    """
    设置csv表格中的属性
    csv only
    :param filename:
    :param attr:
    :param value:
    :return:
    """
    df = pd.read_csv(filename, encoding="utf8")
    df[attr] = value
    df.to_csv(filename, encoding="utf8")


def query(filename, attr):
    """
    查询csv
    csv only
    :param filename:
    :param attr:
    :return:
    """
    df = pd.read_csv(filename, encoding="utf8")
    return df[attr].values[0]


def save_json(obj_dict, filepath, filename):
    with open(os.path.join(filepath, filename), "w", encoding="utf-8") as f:
        data = json.dumps(obj_dict, indent=4, ensure_ascii=False)
        f.write(data)
        print("保存成功")


def dnd():
    """
    生成一组属性, 力量Str、敏捷Dex、体质Con、智力Int、感知Wis、魅力Cha
    :return: list of int
    """
    attr_list = []
    for i in range(6):
        list1 = []
        for j in range(4):
            list1.append(roll(1, 6))
        attr_list.append(sum(list1) - min(list1))
    return attr_list


def ft2m(ft):
    """
    feet convert to meter
    :param ft: 英尺
    :return:
    """
    return ft * 0.3048


def lb2kg(lb):
    return lb * 0.45359237



