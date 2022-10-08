from utis import *
import json
import random
import time

def json_add_user(message):  # функция добовления пользователя
    with open(path_to_baza, "r") as file_js:
        data = json.load(file_js)

    mci = message.from_user.id  # Уникальный ID пользователя 912185600
    chat_username = "@" + str(message.chat.username)  # Ник нейм пользователя (@Andrey_Karm)
    last_name = message.from_user.last_name  # Обязательное имя пользователя (Andrey)
    first_name = message.from_user.first_name  # Не обязательное фамилия пользователя (K)/(None)
    # Врямя первого нажатия на /start пользователем
    creation_time = str(time.strftime("%H:%M:%S:%d:%m:%Y", time.localtime())) + ":" + str(random.randint(1, 99))
    arr_user_info = [chat_username, first_name]
    if last_name is None:
        arr_user_info.append(creation_time)
    else:
        arr_user_info += [last_name, creation_time]
    data["settings"][mci] = arr_user_info

    with open(path_to_baza, "w") as file_js:
        json.dump(data, file_js, indent=2)


def json_user_idias(message, text):  # функция текста
    with open(path_to_baza, "r") as file_js:
        data = json.load(file_js)

    mci = message.from_user.id  # Уникальный ID пользователя 912185600
    chat_username = "@" + str(message.chat.username)  # Ник нейм пользователя (@Andrey_Karm)
    first_name = message.from_user.first_name  # Не обязательное фамилия пользователя (K)/(None)
    # Врямя отправи idias пользователем с случайным числов в конце
    creation_time = str(time.strftime("%H:%M:%S:%d:%m:%Y", time.localtime())) + ":" + str(random.randint(1, 99))
    arr_user_info = [text, mci, chat_username, first_name]
    data["Idias"][creation_time] = arr_user_info

    with open(path_to_baza, "w") as file_js:
        json.dump(data, file_js, indent=2)


def json_is_old_user(chat_id):  # Проверка пользовался ли ботом chat_id
    with open(path_to_baza, "r") as file_js:
        data = json.load(file_js)
    try:
        data["settings"][f"{chat_id}"]
        return True
    except Exception:
        return False


def json_list_user_id():  # функция получения всех пользователей
    with open(path_to_baza, "r") as file_js:
        data = json.load(file_js)
    list_user = []
    for mci in data["settings"]:
        list_user.append(mci)
    return list_user


# Проверка на генераию ref_url
def in_json(ref_url):
    with open(path_to_baza, "r") as file_js:
        data = json.load(file_js)

    for i in data["my_file_id"]:
        if i == ref_url:
            return True
    return False


# Есть ли ref_url в базе
def return_file_type(ref_url):
    with open(path_to_baza, "r") as file_js:
        data = json.load(file_js)
    file_type = data["my_file_id"][ref_url]
    return file_type


# Получение по ref_url file_id
def return_file_id(ref_url):
    with open(path_to_baza, "r") as file_js:
        data = json.load(file_js)
    file_id = data["my_file_id"][ref_url][0]
    return file_id


# Геннерация слуайного набора символов из 170808393600000 различных вариаций
def get_rand_char():
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHILKMNOPQRSTUVWXYZ1234567890'  # нет буквы L
    ref_url = ''
    for i in range(random.randint(5, 8)):
        ref_url += random.choice(chars)
    return ref_url


# Добовление файла в baza
def add_file_info(file_id, content_format, mci, size):
    with open(path_to_baza, "r") as file_js:
        data = json.load(file_js)
    ref_url = get_rand_char()

    while in_json(ref_url):    # точно генерирует уникальный параль
        ref_url = get_rand_char()
    creation_time = str(time.strftime("%H:%M:%S:%d:%m:%Y", time.localtime())) + ":" + str(random.randint(1, 99))
    # 0-file_id 1-тип файла 2-id_user 3 можно отправлять 4-время создания
    arr = [[file_id, content_format, mci, True, creation_time]]

    if size is not None:
        arr.append(round(size / 2 ** 20, 3))
    data["my_file_id"][ref_url] = arr

    with open(path_to_baza, "w") as file_js:
        json.dump(data, file_js, indent=2)
    return ref_url

# Создание и добовление в baza ref_url
def add_file_location(name_location):
    with open(path_to_baza, "r") as file_js:
        data = json.load(file_js)

    ref_url = get_rand_char()
    while in_json(ref_url):
        ref_url = get_rand_char()
    ref_url = "J" + ref_url
    data["my_location"][ref_url] = [name_location, 0, []]

    with open(path_to_baza, "w") as file_js:
        json.dump(data, file_js, indent=2)
    return ref_url


# Получение информации о точки
def return_info_from_location(ref_url):
    with open(path_to_baza, "r") as file_js:
        data = json.load(file_js)
    file_id = data["my_location"][ref_url]
    return file_id


# получение всех id для рассылки
def return_id_file_user():
    with open(path_to_baza, "r") as file_js:
        data = json.load(file_js)
    js_in_list = []
    for ref in data["my_file_id"]:
        if data["my_file_id"][ref][0][2] != admin_id:  # admin_id
            js_in_list.append(data["my_file_id"][ref])
    return js_in_list


# Добовление информации от точки
def add_info_from_location(ref_url, chat_id):
    with open(path_to_baza, "r") as file_js:
        data = json.load(file_js)
    file_id = data["my_location"][ref_url]

    name_location = file_id[0]  # имя точки
    sum_users = file_id[1]  # Количесто пользователей перешедшие из точки
    id_users = list(file_id[2])  # ID пользователей перешедшие из точки
    if not (chat_id in id_users):
        id_users.append(chat_id)
        sum_users += 1
    data["my_location"][ref_url] = [name_location, sum_users, id_users]
    with open(path_to_baza, "w") as file_js:
        json.dump(data, file_js, indent=2)


if __name__ == "__main__":
    print(return_file_type("KXRle"))
