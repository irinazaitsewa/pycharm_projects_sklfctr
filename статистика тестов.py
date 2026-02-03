# Задача: разработать фреймворк для автоматического веб-приложения.
# - создать функцию, которая будет собирать статистику тестов:
# количество проведённых и количество «упавших»;
# - эта информация должна быть доступна в глобальном контексте для последующего вывода в отчёт

tests_run = 0
tests_failed = 0

def run_test(test):
    global tests_run
    global tests_failed
    if test():
        tests_run += 1
    else:
        tests_failed += 1

# Итоговый код для проверки:
# тест 1
def primes(m):
    for num in range(2, m + 1):  # Начнем с первого простого числа — 2 и итерируем до m
        prime = True  # Предполагаем, что число является простым

        # Проверяем делители числа num от 2 до квадратного корня из num
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:  # Если число делится без остатка, оно не является простым
                prime = False
                break  # Прекращаем проверку, так как нашли делитель

        if prime:  # Если число простое, возвращаем его
            yield num
def test_primes_2():
    return list(primes(2)) == [2]

tests_run = 0
tests_failed = 0

def run_test(test):
    global tests_run
    global tests_failed
    if test():
        tests_run += 1
    else:
        tests_failed += 1

run_test(test_primes_2)
print(tests_run, tests_failed)

# тест 2
def primes(m):
    for num in range(2, m + 1):  # Начнем с первого простого числа — 2 и итерируем до m
        prime = True  # Предполагаем, что число является простым

        # Проверяем делители числа num от 2 до квадратного корня из num
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:  # Если число делится без остатка, оно не является простым
                prime = False
                break  # Прекращаем проверку, так как нашли делитель

        if prime:  # Если число простое, возвращаем его
            yield num

def test_primes_1():
    return list(primes(1)) == [1]

tests_run = 0
tests_failed = 0

def run_test(test):
    global tests_run
    global tests_failed
    if test():
        tests_run += 1
    else:
        tests_failed += 1

run_test(test_primes_1)
print(tests_run, tests_failed)

# тест 3
def primes(m):
    for num in range(2, m + 1):  # Начнем с первого простого числа — 2 и итерируем до m
        prime = True  # Предполагаем, что число является простым

        # Проверяем делители числа num от 2 до квадратного корня из num
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:  # Если число делится без остатка, оно не является простым
                prime = False
                break  # Прекращаем проверку, так как нашли делитель

        if prime:  # Если число простое, возвращаем его
            yield num
def test_primes_10():
    return list(primes(10)) == [2, 3, 5, 7]
def test_primes_20():
    return list(primes(20)) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_primes_50():
    return list(primes(50)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def test_primes_100():
    return list(primes(100)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 59, 61, 67, 71, 73, 79, 83, 89, 97]

tests_run = 0
tests_failed = 0

def run_test(test):
    global tests_run
    global tests_failed
    if test():
        tests_run += 1
    else:
        tests_failed += 1

run_test(test_primes_10)
run_test(test_primes_20)
run_test(test_primes_50)
run_test(test_primes_100)
print(tests_run, tests_failed)