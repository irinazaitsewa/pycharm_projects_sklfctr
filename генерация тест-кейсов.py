# Задача: разработка фреймворка для автоматического тестирования веб-сервиса.
# - создать функцию, которая генерирует тест-кейсы;
# - эта функция должна содержать вложенную функцию,
# которая будет увеличивать на 1 возвращать уникальный идентификатор тест-кейса при каждом вызове;
# - изменения значения идентификатора должны сохраняться между вызовами функции next_case().

def generate_test_case():
    case_id = 0

    def next_case():
            nonlocal case_id
            case_id += 1
            return case_id

    return next_case

# Итоговый код для проверки:
# тест 1
def generate_test_case():
    case_id = 0

    def next_case():
            nonlocal case_id
            case_id += 1
            return case_id

    return next_case

case = generate_test_case()
to_test = [case() for _ in range(155)]

print(to_test)