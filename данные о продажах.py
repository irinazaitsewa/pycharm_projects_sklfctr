# Задача: обработать данные о продажах, которые представлены в виде списка списков.
# - Каждый внутренний список представляет собой запись о продаже
# и содержит следующую информацию: ["название товара", количество, цена за единицу];
# - функция принимает список списков
# и ключевые аргументы, которые определяют, какую статистику нужно вернуть:
# общий доход или количество проданных единиц каждого товара;
# - функция должна отрабатывать корректно, если ей были переданы сторонние ключевые аргументы

def sales_stats(data, **kwargs):
   revenue = sum([item[1]*item[2] for item in data]) if kwargs.get('revenue') else None
   if kwargs.get('quantity'):
       quantity = {}
       for item in data:
           if item[0] in quantity:
               quantity[item[0]] += item[1]
           else:
               quantity[item[0]] = item[1]
   else:
       quantity = None
   return revenue, quantity

# Аргументы, передаваемые в метод/функцию:
# тест 1
# [('Apple', 10, 0.5), ('Orange', 5, 0.6)]
# revenue = True
# quantity = True
# print(sales_stats([('Apple', 10, 0.5), ('Orange', 5, 0.6)], revenue = True, quantity = True))
# тест 2
# [('Apple', 10, 0.5), ('Orange', 5, 0.6)]
# revenue = True
# print(sales_stats([('Apple', 10, 0.5), ('Orange', 5, 0.6)], revenue = True))
# тест 3
# []
# revenue = True
# quantity = True
# print(sales_stats([], revenue = True, quantity = True))