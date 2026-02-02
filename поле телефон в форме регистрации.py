# Задача: проверить в форме регистрации на сайте поле «Телефон»:
# -корректная обработка введенных данных;
# -разные форматы;
# Функция приводит номер к единому формату: 1234567890, результат применения функции к списку сохраняется.


phone_numbers = ['123-456-7890', '123.456.7890', '(123) 456-7890', '+1234567890', '1234567890']

def format_phone_number(number):
   return ''.join(filter(str.isdigit, number))

formatted_numbers = list(map(format_phone_number, phone_numbers))

print(formatted_numbers)
