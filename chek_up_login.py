'''Напишите программу, осуществляющую проверку логина и пароля для входа в систему. Проверка данны должна
осуществлятся в отдельной функции, принимающие параметры: имя пользователя, пароль, количество попыток входа в систему
 пог умолчанию 3, сообщение выводимое пользователю в случае если все попытки входа в систему исчерпаны'''
import time


def login_users_func():
    users = {
    'user1': 'pass1',
    'user2': 'pass2',
    'user3': 'pass3',
    }
    attempts = 3
    attempt = 0
    while attempt < attempts:
        login = input('Введите логин:\n>> ')
        password = input('Введите пароль:\n>> ')
        if login in users and users[login] == password:
            print(f'Вы зашли как {login}.')
        else:
            print('Пробуй повторить ввод еще раз через 5 сек\n >>>')
            time.sleep(5)

        attempt += 1
    else:
        print('В журнал админа сделана запись о данном событии.')
        exit()

    print('Выйти: exit + Enter.')
    while True:
        s = input('>> ')
        if s == 'exit':
            print('Вы вышли.')
        break

print(login_users_func())