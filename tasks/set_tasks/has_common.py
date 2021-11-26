"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая возвращает True, если есть общие элементы, и False,
если нет
"""


def has_common(set_1: set, set_2: set) -> bool:
    # TODO вставить код сюда
    for i in set_1:
        if i in set_2:
            return True
    return False


if __name__ == '__main__':
    assert has_common({1, 2, 3, 4}, {3, 4, 5})
    assert not has_common({1, 2, 3, 4}, {6, 8})
    print('Решено!')
