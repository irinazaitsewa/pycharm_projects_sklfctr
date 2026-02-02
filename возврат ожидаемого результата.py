# Задача: написать функцию test_function(), которая принимает:
# -другую функцию, которая принимает один аргумент — имя функции,
# -аргумент для этой функции,
# -ожидаемый результат;
# Функция test_function() должна возвращать True, если функция возвращает ожидаемый результат,
# и False в противном случае.


def test_function(func, arg, expected_result):
   return func(arg) == expected_result


# Итоговый код для проверки:

# тест 1
def square(x):
    return x * x
print(test_function(square, 2, 4))
print(test_function(square, 3, 9))
print(test_function(square, 4, 16))
print(test_function(square, 5, 25))
print(test_function(square, 6, 37))

# тест 2
def is_even(x):
    return x % 2 == 0
print(test_function(is_even, 2, True))
print(test_function(is_even, 3, False))
print(test_function(is_even, 4, True))
print(test_function(is_even, 5, False))
print(test_function(is_even, 6, False))