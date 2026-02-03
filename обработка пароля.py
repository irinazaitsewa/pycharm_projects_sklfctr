# Напишите функцию check_password,
# которая принимает пароль в виде строки и проверяет, что:
# -длина пароля не менее 8 символов;
# -в пароле есть хотя бы одна заглавная буква;
# -в пароле есть хотя бы одна строчная буква;
# -в пароле есть хотя бы одна цифра.

def check_password(password):
   if len(password) < 8:
       print("Пароль должен быть не менее 8 символов")
   upper, lower, digit = False, False, False
   for char in password:
       if char.isupper():
           upper = True
       elif char.islower():
           lower = True
       elif char.isdigit():
           digit = True
   if not upper:
       print("Пароль должен содержать хотя бы одну заглавную букву")
   if not lower:
       print("Пароль должен содержать хотя бы одну строчную букву")
   if not digit:
       print("Пароль должен содержать хотя бы одну цифру")

# Аргументы, передаваемые в метод/функцию:
# тест 1 - '1'
# тест 2 - 'Foof12348'
# тест 3 - 'Foofqwerty'

# УСОВЕРШЕНСТВУЕМ функцию, добавив в неё значения по умолчанию,
# с проверкой параметров:

def is_valid_password(password, min_length=8, require_upper=True, require_lower=True, require_digit=True):
   if len(password) < min_length:
       return False
   has_upper = False
   has_lower = False
   has_digit = False
   for char in password:
       if char.isupper():
           has_upper = True
       if char.islower():
           has_lower = True
       if char.isdigit():
           has_digit = True
   if require_upper and not has_upper:
       return False
   if require_lower and not has_lower:
       return False
   if require_digit and not has_digit:
       return False
   return True

