# Задача: измерить время выполнения функций,
# чтобы оценить их производительность и эффективность.
# - необходимо создать декоратор time_it,
# который будет измерять и выводить время выполнения функций в виде строки:
# "Execution time of '{имя_функции}': {int(время_выполнения)} seconds"

import time
from typing import Callable

def time_it(func: Callable):
   def wrapper(*args, **kwargs):
       start_time = time.time()
       result = func(*args, **kwargs)
       end_time = time.time()
       execution_time = end_time - start_time
       print(f"Execution time of '{func.__name__}': {int(execution_time)} seconds")
       return result

   return wrapper

# Итоговый код для проверки:
import time
from typing import Callable

def time_it(func: Callable):
   def wrapper(*args, **kwargs):
       start_time = time.time()
       result = func(*args, **kwargs)
       end_time = time.time()
       execution_time = end_time - start_time
       print(f"Execution time of '{func.__name__}': {int(execution_time)} seconds")
       return result

   return wrapper

@time_it
def test_func():
    time.sleep(1)

test_func()