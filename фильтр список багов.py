# Задача: написать функцию, которая принимает список багов
# и возвращает список багов только с высокой степенью серьезности ("high").

# Дан список багов, где каждый баг представлен в виде словаря со следующими ключами: id, description, severity;
# severity может быть одним из трех значений: "low", "medium", "high".


def filter_high_severity(bugs):
   return list(filter(lambda bug: bug["severity"] == "high", bugs))


# Аргументы, передаваемые в метод/функцию:

# тест 1
[{'severity': 'medium'}, {'severity': 'high'}, {'severity': 'medium'}, {'severity': 'low'}]
print(filter_high_severity([{'severity': 'medium'}, {'severity': 'high'}, {'severity': 'medium'}, {'severity': 'low'}]))

# тест 2
bugs = [
        {"id": 1, "description": "UI bug", "severity": "low"},
        {"id": 2, "description": "Backend error", "severity": "medium"}
    ]
print(filter_high_severity(bugs))

# тест 3
bugs = [
        {"id": 1, "description": "Critical security flaw", "severity": "high"},
        {"id": 2, "description": "Data loss issue", "severity": "high"}
    ]
print(filter_high_severity(bugs))