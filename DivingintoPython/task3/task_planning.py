# Задача 3. Планирование задач
# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.
from datetime import datetime, timedelta

def get_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    return future_date.strftime('%Y-%m-%d')

def main():
    days = int(input("Введите количество дней: "))
    future_date = get_future_date(days)
    print(f"Дата через {days} дней: {future_date}")

main()

# Введите количество дней: 5
# Дата через 5 дней: 2025-07-05