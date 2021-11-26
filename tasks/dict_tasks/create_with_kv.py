"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Пользователь регистрируется в системе.

Мы получаем словарь с его данными.
Написать функцию save_user, которая добавляет в систему по логину данные пользователя

ПРИМЕРЫ
--------------------------------------------------------------------------------
save_user({
    'login': 'some_user',
    'name': 'Name',
    'age': 30
})

USERS == {
    'some_user': {
        'name': 'Name',
        'age': 30
    }
}
"""
users = {}


def save_user(users_list: dict, user_data: dict) -> dict:
    # TODO вставить код сюда
    users_list.update({user_data['login']: {"name": user_data.get("name"), "age": user_data.get("age")}})
    return users_list


if __name__ == '__main__':
    user = {
        'login': 'some_user',
        'name': 'Name',
        'age': 30
    }
    print(f"Добавляем пользователя: {user['login']}")
    save_user(users, user)
    print('Пользователь успешно добавлен!'
          if users.get('some_user', {}).get('login') is None and users.get('some_user', {}).get('name') == 'Name'
          else 'Ошибка добавления пользователя!')
