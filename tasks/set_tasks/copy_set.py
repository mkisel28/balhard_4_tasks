"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая вернет поверхностную копию множества
"""


def copy_set(collection: set) -> set:
    # TODO вставить код сюда
    collection = collection.copy()
    collection_copy = collection
    return collection_copy


if __name__ == '__main__':
    some_set = {1, 2, 3}
    col_copy = copy_set(some_set)
    assert col_copy is not some_set
    print('Решено!')
