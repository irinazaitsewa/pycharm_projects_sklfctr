# Анализ логов системы при помощи генераторов.
# Логи представлены в виде многострочной строки,
# где каждая строка содержит дату, уровень логирования (INFO, WARN, ERROR) и само сообщение.
#
# - функция-генератор принимает строку с логами
# и фильтрует ее по заданному уровню логирования,
# выдавая только те строки, которые соответствуют этому уровню:
# logs = """\
# 2023-08-15 14:15:24 INFO Starting the system.
# 2023-08-15 14:15:26 WARN System load is above 80%.
# 2023-08-15 14:15:27 ERROR Failed to connect to database.
# 2023-08-15 14:15:28 INFO Connection retry in 5 seconds.
# """
# (принимает многострочную строку — лог, уровень фильтра
# и фильтрует их по заданному уровню логирования,
# выдавая только те строки, которые соответствуют этому уровню)

def log_filter(logs_string, log_level):
   for line in logs_string.split('\n'):
       if line and log_level in line:
           yield line.strip()

# Итоговый код для проверки:
# тест 1
logs = "2023-08-15 14:15:24 INFO Starting the system.\n2023-08-15 14:15:26 WARN System load is above 80%.\n2023-08-15 14:15:27 ERROR Failed to connect to database.\n2023-08-15 14:15:28 INFO Connection retry in 5 seconds.\n"

to_test = list(log_filter(logs, log_level="ERROR"))

print(to_test)