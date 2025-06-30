# Задача 2. Работа с текущим временем и датой
# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.

from datetime import datetime

def get_current_time_info():
    now = datetime.now()
    date_time = now.strftime('%Y-%m-%d %H:%M:%S')
    day_of_week = now.strftime('%A')
    week_number = now.isocalendar()[1]
    return date_time, day_of_week, week_number

def main():
    date_time, day_of_week, week_number = get_current_time_info()
    print(f"Текущая дата и время: {date_time}")
    print(f"День недели: {day_of_week}")
    print(f"Номер недели в году: {week_number}")

main()

# Текущая дата и время: 2025-06-30 23:26:30
# День недели: Monday
# Номер недели в году: 27