# Задача: написать функцию, которая будет возвращать список пользователей,
# отсортированных по уровню активности в порядке убывания.
# Функция sorted должна использоваться с аргументом key и лямбда-функцией;
# Имеются данные об активности пользователей в формате словаря,
# где ключ — идентификатор пользователя, а значение — количество его активностей.


def sort_users_by_activity(user_activity):
   sorted_users = sorted(user_activity.items(), key=lambda x: x[1], reverse=True)
   return [user[0] for user in sorted_users]


# Аргументы, передаваемые в метод/функцию:

# тест 1
{'Alice': 5, 'Bob': 2, 'Charlie': 10, 'David': 7}
print(sort_users_by_activity({'Alice': 5, 'Bob': 2, 'Charlie': 10, 'David': 7}))

# тест 2
{'John': 0, 'Paul': 0, 'George': 0, 'Ringo': 0}
print(sort_users_by_activity({'John': 0, 'Paul': 0, 'George': 0, 'Ringo': 0}))

# тест 3
{'User1': 10, 'User2': 20, 'User3': 30, 'User4': 40}
print(sort_users_by_activity({'User1': 10, 'User2': 20, 'User3': 30, 'User4': 40}))

# тест 4
{}
print(sort_users_by_activity({}))