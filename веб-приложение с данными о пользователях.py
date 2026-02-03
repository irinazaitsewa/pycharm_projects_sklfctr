# Условие: веб-приложение позволяет администраторам
# создавать, просматривать и управлять данными о пользователях.
# Необходимо удостовериться, что приложение корректно обрабатывает данные пользователей
# и предоставляет правильную функциональность для работы с ними.
#
# Необходимо реализовать функции для обработки данных о пользователе:
# • calculate_age(birth_date: str) -> int:
# Функция позволяет вычислить возраст пользователя на основе его даты рождения.
# В контексте тестирования веб-приложения можно использовать эту функцию
# для проверки, корректно ли возраст пользователя отображается в его профиле.
# Здесь понадобится модуль datetime.
# Дата рождения всегда будет поступать в формате «год-месяц-день».
#
# • filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
# Функция фильтрует список пользователей
# и возвращает только совершеннолетних.
# При тестировании приложения можно передать список пользователей в эту функцию
# и проверить, что она правильно фильтрует данные и возвращает только совершеннолетних пользователей.
#
# • generate_username(first_name: str, last_name: str) -> str:
# Функция генерирует уникальное имя пользователя на основе его имени и фамилии.
# В контексте тестирования можно использовать эту функцию для проверки,
# что создаваемые имена пользователей уникальны и соответствуют заданному формату.
# Принцип генерирования заключается в следующем:
# первая буква имени + точка + фамилия, при этом все символы должны быть нижнего регистра.

from datetime import date
from typing import List, Dict, Any

def calculate_age(birth_date: str) -> int:
    birth_date = date.fromisoformat(birth_date)
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    adults = [user for user in users if calculate_age(user['birth_date']) >= 18]
    return adults

def generate_username(first_name: str, last_name: str) -> str:
    username = f"{first_name[0].lower()}.{last_name.lower()}"
    return username

# Итоговый код для проверки:
# тест 1
from datetime import date
from typing import List, Dict, Any

def calculate_age(birth_date: str) -> int:
    birth_date = date.fromisoformat(birth_date)
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    adults = [user for user in users if calculate_age(user['birth_date']) >= 18]
    return adults

def generate_username(first_name: str, last_name: str) -> str:
    username = f"{first_name[0].lower()}.{last_name.lower()}"
    return username


users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '2020-05-15'},
              {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22'},
              {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01'}]
to_test = [calculate_age("1945-06-06"), filter_adults(users_data), generate_username("Lev", "Sergeev")]

print(to_test)

# тест 2
from datetime import date
from typing import List, Dict, Any

def calculate_age(birth_date: str) -> int:
    birth_date = date.fromisoformat(birth_date)
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def filter_adults(users: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    adults = [user for user in users if calculate_age(user['birth_date']) >= 18]
    return adults

def generate_username(first_name: str, last_name: str) -> str:
    username = f"{first_name[0].lower()}.{last_name.lower()}"
    return username


test_birth_dates = [
    "2000-01-01",  # Должно вернуться 24 (если сегодняшняя дата 2024-07-09)
    "1995-12-31",  # Должно вернуться 28 (если сегодняшняя дата 2024-07-09)
    "1980-02-29",  # Должно вернуться 44 (если сегодняшняя дата 2024-07-09)
    "2005-07-09",  # Должно вернуться 19 (если сегодняшняя дата 2024-07-09)
]
# Функция filter_adults
test_users_data = [
    {'first_name': 'Alice', 'last_name': 'Smith', 'birth_date': '2000-01-01'},  # Должна быть включена
    {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1995-12-31'},  # Должен быть включен
    {'first_name': 'Eve', 'last_name': 'Brown', 'birth_date': '2010-01-01'},   # Не должен быть включен
]

# Функция generate_username
test_usernames = [
    ("John", "Doe"),        # Должно вернуться "j.doe"
    ("Alice", "Smith"),     # Должно вернуться "a.smith"
    ("Eve", "Brown"),       # Должно вернуться "e.brown"
]
# Вывод результатов тестов
for birth_date in test_birth_dates:
    print(f"calculate_age({birth_date}): {calculate_age(birth_date)}")

print("Filter adults:")
print(filter_adults(test_users_data))

for first_name, last_name in test_usernames:
    print(f"generate_username({first_name}, {last_name}): {generate_username(first_name, last_name)}")


# ЧТОБЫ УСОВЕРШЕНСТВОВАТЬ, РЕАЛИЗУЕМ СЛЕДУЮЩИЙ НАБОР ФУНКЦИЙ:

from typing import List, Dict, Any
from functools import reduce

def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
    full_names = list(map(lambda user: f"{user['first_name']} {user['last_name']}", users))
    return full_names

def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
    emails1 = set(map(lambda user: user['email'], users1))
    emails2 = set(map(lambda user: user['email'], users2))
    matching_emails = emails1.intersection(emails2)
    return matching_emails

def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    keys = users[0].keys()
    combined_data = dict(zip(keys, zip(*[user.values() for user in users])))
    return combined_data

# Итоговый код для проверки:
# тест 1
from typing import List, Dict, Any
from functools import reduce

def convert_to_full_name(users: List[Dict[str, Any]]) -> List[str]:
    full_names = list(map(lambda user: f"{user['first_name']} {user['last_name']}", users))
    return full_names

def find_matching_emails(users1: List[Dict[str, Any]], users2: List[Dict[str, Any]]) -> set:
    emails1 = set(map(lambda user: user['email'], users1))
    emails2 = set(map(lambda user: user['email'], users2))
    matching_emails = emails1.intersection(emails2)
    return matching_emails

def combine_user_data(users: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
    keys = users[0].keys()
    combined_data = dict(zip(keys, zip(*[user.values() for user in users])))
    return combined_data

users_data = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'},
              {'first_name': 'Bob', 'last_name': 'Johnson', 'birth_date': '1985-10-22', 'email': 'bobJ@gmail.com'},
              {'first_name': 'Lev', 'last_name': 'Sergeev', 'birth_date': '2015-01-01', 'email': 'lev46@gmail.com'},
              {'first_name': 'Anna', 'last_name': 'Smith', 'birth_date': '1988-03-08',
               'email': 'anna.smith@example.com'},
              {'first_name': 'Emily', 'last_name': 'Brown', 'birth_date': '1993-11-28',
               'email': 'emily_brown@hotmail.com'}]

users_data_ext = [{'first_name': 'John', 'last_name': 'Doe', 'birth_date': '1990-05-15', 'email': 'johndoe@gmail.com'},
                  {'first_name': 'Alex', 'last_name': 'Davis', 'birth_date': '2000-09-17',
                   'email': 'alex.davis@gmail.com'},
                  {'first_name': 'Maria', 'last_name': 'Martinez', 'birth_date': '1977-07-12',
                   'email': 'maria.m@example.com'},
                  {'first_name': 'Michael', 'last_name': 'Johnson', 'birth_date': '1972-04-05',
                   'email': 'michaelj@example.net'}]

to_test = [convert_to_full_name(users_data), find_matching_emails(users_data, users_data_ext), combine_user_data(users_data)]

print(to_test)