"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая получает 2 списка и возвращает все уникальные элементы
из этих двух списков
"""


def common_elements(list_1: list, list_2) -> set:
    # TODO вставить код сюда
    # list_1.set(list_2)
    # print(list_2)
    # print(list_1)
    # result = list(set(list_1))
    # print(result)
    # result = {x for x in list_1 if list_1.count(x) in list_1}
    a = set(list_1)
    b = set(list_2)
    result = a | b
    return result


if __name__ == '__main__':
    assert common_elements([1, 2, 3], [2, 3, 4]) == {1, 2, 3, 4}
    print('Решено!')
