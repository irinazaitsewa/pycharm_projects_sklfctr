# Задача: объединить "Ф статистика тестов" и "Ф генерация тест-кейсов"
# - реализовать функцию, которая будет глобально отслеживать
# количество тестов и их статус,
# - а также внутренне обновлять идентификаторы тестов при каждом вызове;
#
# - функция test_case_generator() возвращает вложенную функцию run_test(test).
# Эта вложенная функция должна:
# - увеличивать глобальные переменные tests_run и tests_failed
# для отслеживания количества выполненных и проваленных тестов;
# - увеличивать на единицу и возвращать уникальный идентификатор тест-кейса при каждом вызове;
# - принимать тестовую функцию test,
# запускать ее и обновлять количество проваленных тестов, если тест не проходит.

tests_run = 0
tests_failed = 0

def test_case_generator():
    case_id = 0

    def run_test(test):
        nonlocal case_id
        global tests_run
        global tests_failed
        tests_run += 1
        if not test():
            tests_failed += 1
        case_id += 1
        return case_id

    return run_test

# Итоговый код для проверки:
# тест 1
run_test = test_case_generator()

# Определение тестовых функций
def test1():
    return True  # Успешный тест

def test2():
    return False  # Провальный тест

def test3():
    return True  # Успешный тест

def test4():
    return False  # Провальный тест

# Запуск тестов
print(run_test(test1))  # Ожидаемый вывод: 1
print(run_test(test2))  # Ожидаемый вывод: 2
print(run_test(test3))  # Ожидаемый вывод: 3
print(run_test(test4))  # Ожидаемый вывод: 4

# Проверка глобальных переменных
print(f"Tests run: {tests_run}")       # Ожидаемый вывод: Tests run: 4
print(f"Tests failed: {tests_failed}") # Ожидаемый вывод: Tests failed: 2

# тест 2
run_test = test_case_generator()

# Определение тестовых функций
def test1():
    return True  # Успешный тест

def test2():
    return False  # Провальный тест

def test3():
    return True  # Успешный тест

def test4():
    return False  # Провальный тест

def test5():
    return True  # Успешный тест

# Запуск тестов
print(run_test(test1))  # Ожидаемый вывод: 1
print(run_test(test2))  # Ожидаемый вывод: 2
print(run_test(test3))  # Ожидаемый вывод: 3
print(run_test(test4))  # Ожидаемый вывод: 4
print(run_test(test5))  # Ожидаемый вывод: 5

# Проверка глобальных переменных
print(f"Tests run: {tests_run}")       # Ожидаемый вывод: Tests run: 5
print(f"Tests failed: {tests_failed}") # Ожидаемый вывод: Tests failed: 2