# Задача: написать функцию, которая автоматически создает отчеты.
# Отчет представляет собой строку, которая содержит информацию о среднем доходе
# и общем количестве проданных единиц товара за определенный период;
# Функция должна принимать на вход данные о продажах и функцию, которую нужно использовать для обработки этих данных
# (в том же формате, что и файл "данные о продажах").


def create_report(data, func):
   revenue, quantity = func(data, revenue=True, quantity=True)
   report = f"Средний доход за данный период составил {revenue/len(data)}.\n"
   report += "Количество проданных единиц каждого товара:\n"
   for item, qty in quantity.items():
       report += f"{item}: {qty}\n"
   return report


# Итоговый код для проверки:

# тест 1
def dummy_func(data, **kwargs):
    revenue = 100.0
    quantity = {"Apple": 10, "Orange": 5}
    return revenue, quantity
print(create_report([('Apple', 10, 0.5), ('Orange', 5, 0.6)], dummy_func))

# тест 2
def dummy_func(data, **kwargs):
    revenue = 100.0
    quantity = {"Apple": 10, "Orange": 5}
    return revenue, quantity
print(create_report([('Apple', 10, 0.5)], dummy_func))