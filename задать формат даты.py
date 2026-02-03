# Реализовать функцию format_date(),
# которая принимает дату в формате "гггг-мм-дд"
# и возвращает её в заданном формате;
# функция должна иметь параметр по умолчанию для формата вывода равный "dmy"

def format_date(date, format="dmy"):
   year, month, day = date.split("-")
   if format == "dmy":
       return f"{day}{month}{year}"
   elif format == "mdy":
       return f"{month}{day}{year}"
   elif format == "ymd":
       return f"{year}{month}{day}"
   else:
       return date